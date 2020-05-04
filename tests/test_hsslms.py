# test_pyhsslms.py
#
# Test routines for HSS/LMS Hash-based Signatures.
#
#
# Copyright (c) 2020, Vigil Security, LLC
# All rights reserved.
#
# Redistribution and use, with or without modification, are permitted
# provided that the following conditions are met:
#
# (1) Redistributions must retain the above copyright notice, this
#     list of conditions, and the following disclaimer.
#
# (2) Redistributions in binary form must reproduce the above
#     copyright notice, this list of conditions and the following
#     disclaimer in the documentation and/or other materials provided
#     with the distribution.
#
# (3) Neither the name of the Vigil Security, LLC nor the names of the
#     contributors to this code may be used to endorse or promote any
#     products derived from this software without specific prior written
#     permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE
# COPYRIGHT HOLDERS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS
# OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) REGARDLESS OF THE
# CAUSE AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY
# WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import os
import unittest
import pyhsslms
from pyhsslms.compat import fromHex, toBytes


def mangle(buffer):
    if buffer[30] == 65:
        new_byte = 'B'
    else:
        new_byte = 'A'
    return buffer[0:30] + toBytes(new_byte) + buffer[31:]


class TestLMOTS(unittest.TestCase):

    def testChecksum(self):
        x = fromHex('f0660906f4586869d1618a758223a8e7' + \
                    '0d6c7224080fa4d1436f4906ac7936e9')
        checksum = pyhsslms.checksum(x, 8, 0)
        self.assertEqual(fromHex('1219'), checksum)
        x = fromHex('22810fac106936fb891993ae9d768cb1' + \
                    '399483f6a22fb4d0f6e574a1b95c5722')
        checksum = pyhsslms.checksum(x, 4, 4)
        self.assertEqual(fromHex('1f40'), checksum)

    def testBuildPublic(self):
        S = fromHex('61a5d57d37f5e46bfb7520806b07a1b800000005')
        msg = fromHex('0000000500000004d2f14ff6346af964569f7d6cb880a1b66' + \
         'c5004917da6eafe4d9ef6c6407b3db0e5485b122d9ebe15cda93cfec582d7ab')
        buf = fromHex( '00000004d32b56671d7eb98833c49b433c272586bc' + \
         '4a1c8a8970528ffa04b966f9426eb9965a25bfd37f196b9073f3d4a232feb6' + \
         '9128ec45146f86292f9dff9610a7bf95a64c7f60f6261a62043f86c70324b7' + \
         '707f5b4a8a6e19c114c7be866d488778a0e05fd5c6509a6e61d559cf1a77a9' + \
         '70de927d60c70d3de31a7fa0100994e162a2582e8ff1b10cd99d4e8e413ef4' + \
         '69559f7d7ed12c838342f9b9c96b83a4943d1681d84b15357ff48ca579f19f' + \
         '5e71f18466f2bbef4bf660c2518eb20de2f66e3b14784269d7d876f5d35d3f' + \
         'bfc7039a462c716bb9f6891a7f41ad133e9e1f6d9560b960e7777c52f06049' + \
         '2f2d7c660e1471e07e72655562035abc9a701b473ecbc3943c6b9c4f2405a3' + \
         'cb8bf8a691ca51d3f6ad2f428bab6f3a30f55dd9625563f0a75ee390e385e3' + \
         'ae0b906961ecf41ae073a0590c2eb6204f44831c26dd768c35b167b28ce8dc' + \
         '988a3748255230cef99ebf14e730632f27414489808afab1d1e783ed04516d' + \
         'e012498682212b07810579b250365941bcc98142da13609e9768aaf65de762' + \
         '0dabec29eb82a17fde35af15ad238c73f81bdb8dec2fc0e7f932701099762b' + \
         '37f43c4a3c20010a3d72e2f606be108d310e639f09ce7286800d9ef8a1a402' + \
         '81cc5a7ea98d2adc7c7400c2fe5a101552df4e3cccfd0cbf2ddf5dc6779cbb' + \
         'c68fee0c3efe4ec22b83a2caa3e48e0809a0a750b73ccdcf3c79e6580c154f' + \
         '8a58f7f24335eec5c5eb5e0cf01dcf4439424095fceb077f66ded5bec73b27' + \
         'c5b9f64a2a9af2f07c05e99e5cf80f00252e39db32f6c19674f190c9fbc506' + \
         'd826857713afd2ca6bb85cd8c107347552f30575a5417816ab4db3f603f2df' + \
         '56fbc413e7d0acd8bdd81352b2471fc1bc4f1ef296fea1220403466b1afe78' + \
         'b94f7ecf7cc62fb92be14f18c2192384ebceaf8801afdf947f698ce9c6ceb6' + \
         '96ed70e9e87b0144417e8d7baf25eb5f70f09f016fc925b4db048ab8d8cb2a' + \
         '661ce3b57ada67571f5dd546fc22cb1f97e0ebd1a65926b1234fd04f171cf4' + \
         '69c76b884cf3115cce6f792cc84e36da58960c5f1d760f32c12faef477e94c' + \
         '92eb75625b6a371efc72d60ca5e908b3a7dd69fef0249150e3eebdfed39cbd' + \
         'c3ce9704882a2072c75e13527b7a581a556168783dc1e97545e31865ddc46b' + \
         '3c957835da252bb7328d3ee2062445dfb85ef8c35f8e1f3371af34023cef62' + \
         '6e0af1e0bc017351aae2ab8f5c612ead0b729a1d059d02bfe18efa971b7300' + \
         'e882360a93b025ff97e9e0eec0f3f3f13039a17f88b0cf808f488431606cb1' + \
         '3f9241f40f44e537d302c64a4f1f4ab949b9feefadcb71ab50ef27d6d6ca85' + \
         '10f150c85fb525bf25703df7209b6066f09c37280d59128d2f0f637c7d7d7f' + \
         'ad4ed1c1ea04e628d221e3d8db77b7c878c9411cafc5071a34a00f4cf07738' + \
         '912753dfce48f07576f0d4f94f42c6d76f7ce973e9367095ba7e9a3649b7f4' + \
         '61d9f9ac1332a4d1044c96aefee67676401b64457c54d65fef6500c59cdfb6' + \
         '9af7b6dddfcb0f086278dd8ad0686078dfb0f3f79cd893d314168648499898' + \
         'fbc0ced5f95b74e8ff14d735cdea968bee74')
        expected_pub = fromHex('87be83923a22106731e8f10f826faf4d02' + \
         '17b07d99694d1174d350fba7d578a1')
        sig = pyhsslms.LmotsSignature.deserialize(buf)
        pub = sig.buildPublic(S, msg)
        self.assertEqual(expected_pub, pub)

    def testKnownPrivateKey(self):
        msg = toBytes('The way to get started is to quit talking and ' + \
                      'begin doing.')
        S = fromHex('c6d47a98577cd2f13007908fd14309ca00000001')
        seed = fromHex('1e305866bfc4d18c4735bfc677711109' + \
                             'a886656dc432e39281bc5a129b518172')
        prv = pyhsslms.LmotsPrivateKey(S=S, SEED=seed)
        self.assertEqual(1, prv.remaining())
        self.assertFalse(prv.is_exhausted())
        sigbuffer = prv.sign(msg)
        self.assertEqual(1124, len(sigbuffer))
        self.assertEqual(0, prv.remaining())
        self.assertTrue(prv.is_exhausted())
        sig = pyhsslms.LmotsSignature.deserialize(sigbuffer)
        pub = prv.publicKey()
        self.assertTrue(pub.verify(msg, sigbuffer))
        self.assertFalse(pub.verify(msg, mangle(sigbuffer)))
        self.assertFalse(pub.verify(mangle(msg), sigbuffer))
        self.assertTrue(sig.prettyPrint())
        prvpp = prv.prettyPrint()
        self.assertIn('LMOTS type: 00000004', prvpp)
        self.assertIn('S         : c6d47a98577cd2f13007908fd14309ca', prvpp)
        self.assertIn('SEED      : 1e305866bfc4d18c4735bfc677711109', prvpp)
        pubpp = pub.prettyPrint()
        self.assertIn('S         : c6d47a98577cd2f13007908fd14309ca', pubpp)

    def testRandomPrivateKey(self):
        msg = toBytes('The way to get started is to quit talking and ' + \
                      'begin doing.')
        prv = pyhsslms.LmotsPrivateKey()
        sigbuffer = prv.sign(msg)
        sig = pyhsslms.LmotsSignature.deserialize(sigbuffer)
        pub = prv.publicKey()
        self.assertTrue(pub.verify(msg, sigbuffer))
        self.assertFalse(pub.verify(msg, mangle(sigbuffer)))
        self.assertFalse(pub.verify(mangle(msg), sigbuffer))
        self.assertTrue(sig.prettyPrint())
        self.assertTrue(prv.prettyPrint())
        self.assertTrue(pub.prettyPrint())


class TestLMS(unittest.TestCase):

    def testKnownPrivateKey(self):
        lmots_sha256_n32_w8 = pyhsslms.lmots_sha256_n32_w8
        lms_sha256_m32_h5 = pyhsslms.lms_sha256_m32_h5
        msg = toBytes('The way to get started is to quit talking and ' + \
                      'begin doing.')
        buffer = fromHex('0000000500000004' + \
                         '0c0fe552dcf77d4bbe16b28605759ea4' + \
                         'bb06873c809d0b9a00d753deec2e5845' + \
                         'e4a9fccb86dc9c49d71b72d5696acb54' + \
                         '00000000')
        prv = pyhsslms.LmsPrivateKey.deserialize(buffer)
        self.assertEqual(32, prv.remaining())
        sigbuffer = prv.sign(msg)
        self.assertEqual(1292, len(sigbuffer))
        self.assertEqual(31, prv.remaining())
        self.assertFalse(prv.is_exhausted())
        sig = pyhsslms.LmsSignature.deserialize(sigbuffer)
        pub = prv.publicKey()
        self.assertTrue(pub.verify(msg, sigbuffer))
        self.assertFalse(pub.verify(msg, mangle(sigbuffer)))
        self.assertFalse(pub.verify(mangle(msg), sigbuffer))
        self.assertTrue(sig.prettyPrint())
        prvpp = prv.prettyPrint()
        self.assertIn('LMS type  : 00000005', prvpp)
        self.assertIn('LMOTS type: 00000004', prvpp)
        self.assertIn('I         : e4a9fccb86dc9c49d71b72d5696acb54', prvpp)
        self.assertIn('SEED      : 0c0fe552dcf77d4bbe16b28605759ea4', prvpp)
        self.assertIn('pub       : a8b35f4c521183a05d81fbcf8a81ffc9', prvpp)
        pubpp = pub.prettyPrint()
        self.assertIn('I         : e4a9fccb86dc9c49d71b72d5696acb54', pubpp)
        self.assertIn('K         : a8b35f4c521183a05d81fbcf8a81ffc9', pubpp)

    def testRandomPrivateKey(self):
        msg = toBytes('The way to get started is to quit talking and ' + \
                      'begin doing.')
        prv = pyhsslms.LmsPrivateKey()
        sigbuffer = prv.sign(msg)
        sig = pyhsslms.LmsSignature.deserialize(sigbuffer)
        pub = prv.publicKey()
        self.assertTrue(pub.verify(msg, sigbuffer))
        self.assertFalse(pub.verify(msg, mangle(sigbuffer)))
        self.assertFalse(pub.verify(mangle(msg), sigbuffer))
        self.assertTrue(sig.prettyPrint())
        self.assertTrue(prv.prettyPrint())
        self.assertTrue(pub.prettyPrint())


class TestHSS(unittest.TestCase):

    def testKnownPrivateKey(self):
        msg = toBytes('The way to get started is to quit talking and ' + \
                      'begin doing.')
        buffer = fromHex('00000002000003ff0000000500000004' + \
                         '3df0eddf9856dea6d6d89135515c04d3' + \
                         '37a692dd8879b5ef3ec58f3a9bcc7595' + \
                         'ee9a2418209ce10bc035de0f55c5eecf' + \
                         '00000000')
        prv = pyhsslms.HssPrivateKey.deserialize(buffer)
        self.assertEqual(1023, prv.remaining())
        sigbuffer = prv.sign(msg)
        self.assertEqual(2644, len(sigbuffer))
        self.assertEqual(1022, prv.remaining())
        self.assertFalse(prv.is_exhausted())
        sig = pyhsslms.HssSignature.deserialize(sigbuffer)
        pub = prv.publicKey()
        self.assertTrue(pub.verify(msg, sigbuffer))
        self.assertFalse(pub.verify(msg, mangle(sigbuffer)))
        self.assertFalse(pub.verify(mangle(msg), sigbuffer))
        self.assertTrue(sig.prettyPrint())
        prvpp = prv.prettyPrint()
        self.assertIn('levels    : 2', prvpp)
        self.assertIn('LMS type  : 00000005', prvpp)
        self.assertIn('LMOTS type: 00000004', prvpp)
        self.assertIn('q         : 00000001', prvpp)
        self.assertIn('I         : ee9a2418209ce10bc035de0f55c5eecf', prvpp)
        pubpp = pub.prettyPrint()
        self.assertIn('levels    : 2', pubpp)
        self.assertIn('I         : ee9a2418209ce10bc035de0f55c5eecf', pubpp)
        self.assertIn('K         : c584f571bbfdf285b9a8ac5bafb7738a', pubpp)

    def testSmallRandomPrivateKey(self):
        msg = toBytes('The way to get started is to quit talking and ' + \
                      'begin doing.')
        prv = pyhsslms.HssPrivateKey(levels=1)
        sigbuffer = prv.sign(msg)
        sig = pyhsslms.HssSignature.deserialize(sigbuffer)
        pub = prv.publicKey()
        self.assertTrue(pub.verify(msg, sigbuffer))
        self.assertFalse(pub.verify(msg, mangle(sigbuffer)))
        self.assertFalse(pub.verify(mangle(msg), sigbuffer))
        self.assertTrue(sig.prettyPrint())
        self.assertTrue(prv.prettyPrint())
        self.assertTrue(pub.prettyPrint())
        
    def testMediumRandomPrivateKey(self):
        msg = toBytes('The way to get started is to quit talking and ' + \
                      'begin doing.')
        prv = pyhsslms.HssPrivateKey(levels=2)
        sigbuffer = prv.sign(msg)
        sig = pyhsslms.HssSignature.deserialize(sigbuffer)
        pub = prv.publicKey()
        self.assertTrue(pub.verify(msg, sigbuffer))
        while(not prv.is_exhausted()):
            sigbuffer = prv.sign(msg)
        with self.assertRaises(ValueError):
            failed_sigbuffer = prv.sign(msg)
        sig = pyhsslms.HssSignature.deserialize(sigbuffer)
        pub = prv.publicKey()
        self.assertTrue(pub.verify(msg, sigbuffer))
        self.assertFalse(pub.verify(msg, mangle(sigbuffer)))
        self.assertFalse(pub.verify(mangle(msg), sigbuffer))
        self.assertTrue(sig.prettyPrint())
        self.assertTrue(prv.prettyPrint())
        self.assertTrue(pub.prettyPrint())

    def testLargerRandomPrivateKey(self):
        msg = toBytes('The way to get started is to quit talking and ' + \
                      'begin doing.')
        prv = pyhsslms.HssPrivateKey(levels=4)
        sigbuffer = prv.sign(msg)
        sig = pyhsslms.HssSignature.deserialize(sigbuffer)
        pub = prv.publicKey()
        self.assertTrue(pub.verify(msg, sigbuffer))
        self.assertFalse(pub.verify(msg, mangle(sigbuffer)))
        self.assertFalse(pub.verify(mangle(msg), sigbuffer))
        self.assertTrue(sig.prettyPrint())
        self.assertTrue(prv.prettyPrint())
        self.assertTrue(pub.prettyPrint())


class TestHSSLMS(unittest.TestCase):

    def testGenSignSignVerifyVerifyFailFail(self):
        fname = 'test1234.txt'
        keyname = 'testsigkey'
        # make sure the files that will be created do not already exist
        self.assertFalse(os.path.exists(fname))
        self.assertFalse(os.path.exists(fname + '.sig'))
        self.assertFalse(os.path.exists(keyname + '.prv'))
        self.assertFalse(os.path.exists(keyname + '.pub'))
        msg = toBytes('This is a test message to be signed.\n')
        prv_key = pyhsslms.HssLmsPrivateKey.genkey(keyname, levels=2)
        self.assertTrue(prv_key)
        self.assertTrue(os.path.exists(keyname + '.prv'))
        self.assertTrue(os.path.exists(keyname + '.pub'))
        with open(fname, 'wb') as f:
            f.write(msg)
        self.assertTrue(os.path.exists(fname))
        self.assertTrue(prv_key.signFile(fname))
        self.assertTrue(os.path.exists(fname + '.sig'))
        sigbuf = prv_key.sign(msg)
        self.assertTrue(len(sigbuf))
        pub_key = pyhsslms.HssLmsPublicKey(keyname)
        self.assertTrue(pub_key)
        self.assertTrue(pub_key.verifyFile(fname))
        self.assertTrue(pub_key.verify(msg, sigbuf))
        self.assertFalse(pub_key.verify(msg, mangle(sigbuf)))
        self.assertFalse(pub_key.verify(mangle(msg), sigbuf))
        os.remove(fname)
        os.remove(fname + '.sig')
        os.remove(keyname + '.prv')
        os.remove(keyname + '.pub')

    def testFromPublicKeyGetI(self):
        keyname = 'testpubkey'
        # make sure the file that will be created does not already exist
        self.assertFalse(os.path.exists(keyname + '.pub'))
        buffer = fromHex('000000010000000500000004' + \
                         '616d2133c3275326e591f26c748e3588' + \
                         '9ab949c09b231bc43a2748486ba78492' + \
                         '190208cf5a3d8491e774d8301dc8510a')
        expected = fromHex('616d2133c3275326e591f26c748e3588')
        with open(keyname + '.pub', 'wb') as pub_file:
            pub_file.write(buffer)
        pub_key = pyhsslms.HssLmsPublicKey(keyname)
        I = pub_key.I()
        self.assertEqual(expected, I)
        os.remove(keyname + '.pub')

class TestInterop(unittest.TestCase):

    def testVerifyHashSigs(self):
        msg = fromHex('5468697320697320612074657374206d6573736167652' + \
         '0746f206265207369676e65642e0a')
        pubbuffer = fromHex('000000020000000500000004' + \
         '616d2133c3275326e591f26c748e35889ab949c09b231bc43a2748486ba78492' + \
         '190208cf5a3d8491e774d8301dc8510a')
        sigbuffer = fromHex('000000010000000000000004' + \
         '19c1e5adebca8c25313c3d0060d9373bbfbe75fdfedef7321f08d99f763eadbd' + \
         '86774810914ff571cd5d61c5e3364cd215f4baaee6a88901c878d3a1f47fd621' + \
         'f6c0433c75fcc106a6f530f543b946a700d4a998a51448eb448c422f86b4760f' + \
         '22573c72b8c497d0e77260f5703386188898a00c612e21b226629af4a5ed4fa0' + \
         'bef780407ccc75ab54a2c3246a7f268569f06e8b2e553b2dcb5237bb0d144a2a' + \
         '968844103741e09ed5e604ded124a49b028d6548aa0fe014b420598d68a251a4' + \
         '510582062a2695a96056f606c07bb8cfa9de87a6ce1f734c8f793b5853dc05b2' + \
         '1bb3ddecce509d7b4514c5b823f6970696e73cbeff3700f9e3ce2a45ec057477' + \
         '9d229c340a2d37bbd54b0483240c0b6cca3d27ede4910fca621e03ebd0aee22d' + \
         'fce1f4be9fc9473b6427d48464806878e624c77b20aee4d18834525649e6826e' + \
         'fb6b2cd068619193c4204831ddaed01b0be3275be23cdfccc9b7eff52678b3cd' + \
         'e11315ad936872f5d14573cb0b94e3350fa92a6e3099f6ed34665640145a2866' + \
         'bd4dbd6f7bfe4897d30ba701be0f9d47fe384f0bc11ecd9628d4797732a77e15' + \
         '0726a8756f3054ef7f52cd4eadf6732506f2b738af77eb85c55dc412f25052b1' + \
         'cd6b8d0fb916687420f3587106daf3e390a8837716fec4bc8cb314af1ed11d71' + \
         '35ef40800e281a0c44089e066f501e64ee2eae65603e747e14034a2d5a344172' + \
         '9d2d124dfb90d6d78c095a8196dbd064543ffff184a774292ea7be195fcaf039' + \
         '25ace1c9cf625798ee1725f2544290b81a86ae2fa213b1e5b7a78250bbceaf27' + \
         '476ced5b04adbe0794a11ec3ea3b3adbc885d270700021edb6d2a6df15470db4' + \
         'd58fd24bfeeda6cb0e1a119dc5c7a8819abf4c4ed7e8ed03cb834db8e73073a7' + \
         '23ba6a2e475dbad63dbac768fd1e4ef66649e1780bd1ea2e6dc0705106880e9c' + \
         'b9bc641808248d2030d95dbdcba485ae4f11df726b106bb6caebb3a379dfad9f' + \
         '807c1c97f73941382766d90a5a6b902bad9c81d5a1a58420bffe0a26b28616a2' + \
         'c65512b5e137a838d91bfb160e84ec0169091098abacafa537918ed29217a9d4' + \
         'd8001ca0d05e31a5fa39eca9d89ed4355d25ab05621c46636fb8dafdde5408da' + \
         'ec262285675df50be528d7673b745fd6df89c1f091b432dbad633b1c8eb35cee' + \
         'f58ec6078e2dd6bd47cd12120bff70a4628a61a507fe9774e9fa90f7486c5fb6' + \
         '0ddd9c14dfe1540768e64a036a6e3e57ee9f00765401227c0a77c81e61f59c4f' + \
         'd217bfd342617a922e03bf16a96d69e142a25cc3c1964be7de3f416ac32b494b' + \
         '726d9c583578e8b54f28803b19b3cca8155485fa06a2512cbd84d2d876ba01db' + \
         'c554db4df25d939685dead655d0b047879e6f1dfc7c4984ec32edd12ac8f9ad9' + \
         '68a56d8eb3af863539db84b88840a79b0e200c7bdf1e0db402464c263fa2b12a' + \
         '0f55baefa4650dc9e0c70a0b115becfd10b49eb3f7e566a7d60115e461875625' + \
         '6c8ecf2a95850a18426f79ec70e4508407e7c8b297e0fdc8350e0ab2c352684f' + \
         '1ef9bb97f47eccfff0badb36c040a10b922b5a5691df0cdf1e50bf908ab8f4f4' + \
         '0000000522572d3011b5d9a4212ade8ee3e9c93393066a83bd28fad993d4e8d2' + \
         'f992f456407fd2405c28d4f063cfd5dd5944e29d73fdadd1986242407dac73af' + \
         '3b7163dbc999afc5fcfd100c53ca4e22d2d2157a44a7699596fedb96e03e29a9' + \
         '23a2a4c227cc7318ed9164f9d5b0b942635392484929ad31bcbaa23e785a72dd' + \
         '483f7c1f6f5b8f5f6e07de9451267e647af09adc8a3f15d3cb29ff87873563fe' + \
         'd0b5931c0000000500000004809ed32be95fb6d01915f606d0d02eb527479101' + \
         '96c7aca46e5d6344c1b1e3b26c7e6ee14c183542ddcc6d69490717d400000002' + \
         '0000000482fa02475f9de33ea21cf5da3a6b8fec729ddfe963befa915f0f8db7' + \
         '3374e1d3699d6e4d7ea4f785d162595ba73b6243a8cefad1663cdae5f58a2d1f' + \
         '712c01113b06ffceee0ade3b9aeab14a09139ab4355b17e087a3adb0a6de6167' + \
         '6cef3fc57d6be0ad58c370a2b100645e009aa94263414150f3b05e7cdceb91ac' + \
         '02039ca08b258ead263ed918954108735643068f23c771ea55912f36461f9998' + \
         '3d8e4fd18f97c7dc39f470fde9c4b23ace60caa60be2f0e1319d72c49387b26d' + \
         'c1f1d3a38aaa64086c7ff91e418990264b21de5a5ede207e7d1b0867045f95d9' + \
         '1b7ed27be026388f8c06043e78476a5b9606c5f72fd0505c9fdfe9ba692ae3ec' + \
         'caadbb2a4036b2a0fc2a278cb6e4905ac71eabaed4cb86bcacf72d92f9b0c977' + \
         '4cdf38888e4c13e17665942ee5227a96f03c6f3eb9849250a1b8ef1449659133' + \
         '7768e198b90a7bcd77e859906a733062b1a6c7990e05ff748f864f3af1d6aa3f' + \
         '13896d0635f1f3848c9e3b4c606ba2d8b232b6728c47fd7fd4cb02ef49c34fc2' + \
         '398dbefc87a65d90c49c685ac14021adf7da235d6a1a9a24e8d5b529ae61092a' + \
         '16de15f57d80c8f3d51c33aa2207d2a3d05f3ae7260df96e52c473d38761d274' + \
         '2143d4d9e56e4d942cb329e5dbd2b8c7da6a0bdba37efc770833a284f7f57634' + \
         '9e63c5b6c81b6f0065f695616fdb4337639e1cc4c73e807debdbe9712655f70c' + \
         'fa7c7f0770460c9d14bc70f55558440c3b02decbffbb341064b5f04e3c1f844e' + \
         '86d3136a4cb778befd0a5cb6e9f45e384814fc7aa8eda544ff222ad5d8501613' + \
         'fdcb3c896ecbd3db6ca96c382b7cf698582620fd17dcf6eae3440acbd43835a0' + \
         'd0b4f491ebb8b49aa393db41ed383acab93daba86d5fb93a388667fc5bf2c664' + \
         'd0d93c52d81895e0587608e7ec4c5a2f82c739654805a82f307e89e2482aca16' + \
         '53865ef7e336d97e6c173ee77cdb4e145ede0fd359d50079dc4c3a477e095906' + \
         '31e06a1e5cdb0f843828499992f9267948e99dceb948fb12330b28a14be0a5ee' + \
         '132a62fda5cb3e27d1cf8a02ebfa7753249cfe23191d74dedc9b09b946796a6d' + \
         '0c51f204836ad47328a77aeea28dd67ddf614c934ecefd6c5d2105fc30ae9149' + \
         '7aeab41fc930ce068d9ebe2d0e0bd036595354eabcc3114441b1a9c96e9c247e' + \
         'bda9c3a43e4fe797b493fc90a661cf27efcc5f83f088f8f85eb150778da5098a' + \
         'b2e425c3e687774b9f39998cecb068f5beb3baae632591f9281f79de13c882ec' + \
         '4762d2d99b2bd50a1d9822b4c8672e7e2d7646b87e88f4d7ce0dc260dadb2655' + \
         '9b31708cf4cc01f3c4564bb38fb73fc5f0adb90d9a135e0230a1542d2e84c2b3' + \
         'adccd39b933a62bd84e819b47c1b28dcebd6018f45e5580c80ea950c67f387e0' + \
         '83e9015bf8343ca2858c3e5e747b5fd8575fd3afa036780cd9e7d9a8c5e8d7ff' + \
         '7673b7481b269f867709e53646f5a628cf363d96ab5e09e5e352acab1542a238' + \
         'cad97cce0ae60e63abff53fecb69687d10a4fb6fe3f696404d62541f82ee1bf9' + \
         'cd3b877a861b4eabef6610dac49c4dd583186ae0658d6e61ea8b8f5189db89dd' + \
         '78207a020000000528439cb3612a7df5c43968f2dcca8945bf397e998f13be92' + \
         'f8a584bb9c9b8eb56c5b8aab9f7851d9ec40fc73ecf6e6b4ee4fa30b080e4aec' + \
         'c3aea0c102b94cc3d2950ab92808cd864f26ca5eaed6623efec6a88d9b0b56d2' + \
         'e73d876b6752e4e925d7d60c46d761f4ebe04fc9e5ff79118e61b5fb12989cb4' + \
         'ac93335d108853eeac4aae6c0d3cd7d35df1d1e3834d8770b81f1584a3a88dfd' + \
         'b55c4fa171ed01d8')
        pub = pyhsslms.HssPublicKey.deserialize(pubbuffer)
        self.assertTrue(pub.prettyPrint())
        sig = pyhsslms.HssSignature.deserialize(sigbuffer)
        self.assertTrue(sig.prettyPrint())
        self.assertTrue(pub.verify(msg, sigbuffer))
        self.assertFalse(pub.verify(msg, mangle(sigbuffer)))
        self.assertFalse(pub.verify(mangle(msg), sigbuffer))

    def testVerifyHashSigsMixedSizeTrees(self):
        msg = fromHex('5468697320697320612074657374206d' + \
         '65737361676520746f206265207369676e65642e0a')
        pubbuffer = fromHex('000000020000000700000003f171a152' + \
         'fd41c92fa7f0d03544804d5a797e49fcbee2a4fde957e62b164c777895a7d224' + \
         'c36341672b8d780e5745fb8f')  
        sigbuffer = fromHex('0000000100000000000000037f6fc2f2' + \
         '6894aeef79f3d8fdc8e67879b18ef0c1e916488fcb400ce544b46076d1535759' + \
         'e09256dfad9898e0ee1ff03e8b3cdcce9b73327e3ef5eeacc037e073b3221eac' + \
         'e8f572c4df1876fc3ed728f515b06e6a5c8d8b08734afa370e35c20a16be184f' + \
         'd5471e75bdf79c679ed287c5b8cb39da361aef6845caea75709673f44b6d38a7' + \
         'a41d3a348349b26315d67ce2f0c06b5aff9406952f44e188de4eb0284075b8f5' + \
         '40a3fb8d5d51169e33596f5da6c46858bdf88cddd5a5eba032bd96df1f5732cb' + \
         'f27bec095afacf81f2c23df7145e43775613775c0e664e8a6969249fe97bafd4' + \
         '760228a27220ab3cd5c0011a6090cb653d8e14bc9e4bc8c75efaacd40426edf0' + \
         '1657fed67ae1448e289e8c913a20bb4d37c47a55e3ea6216afd5727fcb014ac0' + \
         'af50ee3008dc6472bb117ccba23a7d5175029b67f2e621f7ac7f73cdf7ebf318' + \
         '0de474f46b11c9cad7c4b96fed563834ccdf1f746a4a8cb9d01aadb08549126e' + \
         '4c87ab8222cd6c24e8da24708a18d3c15d68744ba7429f1fa72aa676f8c53e18' + \
         'ed60748d85faad03eb7e5c08b6951ae16577086aca8b22eb2d7017837d8904f2' + \
         'cc504cae217e16cacff56dc84496b6b0075b8bca6ce2559921a6e2e72606165d' + \
         'a2913c8ea85f44dd6911e51238292ce225e771c272260f0d02483aeeae117442' + \
         '83269c2bd6970e389e41fbb46371237e7036c4ef42a6ace55794290c1ecc49bd' + \
         '6dbdc565ad4011de91475e0b155a8bad8f9484834eb7aab2f52bb2c934d2bf95' + \
         '85676eda08091a9ab266df063a6e284d9355ea8cafb5bbc20fc627b194967f3c' + \
         '449af0ebd1e14f7ca10975b63f4ed86bed6c5d0f4fe21a3da13fd6b27db99b6a' + \
         'a9eeb68a9365c81edd4f041e0d9e8954475318065206d3fd37385e2986d285ac' + \
         'feead6b3029442ba449747466a5a533e8663310289b19a64ce9db01bf517a02a' + \
         '263d2114c45fe81647e3c5bfb145edefee34a842d3cd40977ac4a46085439c7d' + \
         'c64a541866c16010593bc5abad766266a2d4be0e9738d29c73eb56ddf28824a4' + \
         'b097176091000bdbc44b0299f12f94ebb867aec1664a1a7c81f72157a94a75e8' + \
         'b085885a7546c2570411eebde74107b7d83d967b7c64d99e7135f05015d1087b' + \
         '314be6deb392e102b09aae2f97ac52ccd58d6d4f69fbacf5f2a0dce3c4ab67e0' + \
         '99caaef2295ee1098acbf5eeac29b93f2d273a49d3a45760062adef91687cdb4' + \
         '14319ea0f673bcd351b362b498ae144595e6b6d26cb6c2981be55267be7c1eda' + \
         'acdfc7a7e4ca1f48b06ce40280a9f6eceb4a3aac74bad9fbfd3f78a1e97a1b47' + \
         'f6a5aa590ccb73246fc2ffe733f62aed86fc551a874f9d59f1c63b9e4e4056b8' + \
         '61ce9cc5e2b72aa3ecff1eba6f3e32b761dac5b303f4d5d7823766d035373176' + \
         '121fb73e8f2bdd5438cf55a777760fd31e2757fda6f7010ec912ef7a3d5bdeea' + \
         'c9601cc1e4d4441a2530cc3e3479c3d28caee062c8f8fece091f50aeb2b2c8da' + \
         '4fbc32665c2364a26e777842160b13147042a0a4a23a9028e1eb58538f306ae7' + \
         '849f542a66cccc87affb6c64793e0e37458ebc17f419dfbe12f021bbc099ac6a' + \
         '4fb3f738723763177ff9e5856428c556d7674bb9f7e43f2d3796ba6303bfd2ff' + \
         '5876c02a4c6aa3c7de55660af6c037a2cd744918494ceca61af101f2fcbde546' + \
         '39c07f3950f267c12e9347cf6cb90fe24959c27ef9be55531a499cd0fc8b959e' + \
         '11e7b0a34e3d169dd1873c62d1321d74bc35c80f40c7043c50d78c3605ea1a77' + \
         'fd169d2571fd4f7245ada2cdda2f800ca20820e8f09353a5c278ea166660d9cf' + \
         '1fbaf0560acfa3c968ae4f85d92d9c78f42ed7a3b6e82e9804c8b1e86c86dfca' + \
         '8a9f9ca1eb091847059e0dfe5000f3d4bc8861d6909a7923ddfba4c4cb908370' + \
         '3d6125782488d766b102cb511b4da78cae738541f7e1cc619315ff16df4b8259' + \
         '7307b59f5be7225df1422e36101d02306470b157c00f1c00a281076cf4a21862' + \
         '87d616f04b601c0c7d4ca84cb1a8ab6ad58fcb1b2eb0778203cd484770bb6665' + \
         '226abdd80b72d1e67c5b59e1f1aebadd9a2eabddf568286c07921ea2c491909d' + \
         'c7356dcef436e12a067e929da271ac1a3871dc95d2bd68fd5a41c2a3400db31a' + \
         'cdae6b596af8c72e8d8c33096e3f60725b841d72e2176deee99db6c27b544bff' + \
         '5a41cba4b2cff7e5a8a79c93eae59ea3febcc9398434420cd39be9629716da47' + \
         '568a7b6389e43a632d11e5a626a1d584d86a1d0383edd7e0a808c0e76b741db9' + \
         '5e114c48c3fa37db0df0c8f690e6a77b161f154418f1b2aab43edc6233571c73' + \
         '970df7e7eade6a4d7149c1aa7de1e6a32a7e7f919f261c7193481e06417a9295' + \
         '40e697e6938ba2195b521a4e1aaa3498f51fbae169d86f4ea4ebb7d65ce0251e' + \
         '96a1da90e2a864abf0d1c241b44901d4d6b310084f0a795ade9abb85acb91c1b' + \
         '917c48c933c8ac08c1c17cc8e36eb1b1f74a7db162f008e06a8f4b5d28eb0d7b' + \
         '88c7a3cf654fb9a64579717d659e333e3169e75d03902fe147bea092a84a7bb6' + \
         '92bc28afd59e34df09cd5e4bc29c6f7c0248ce87640d974ae2b31318443524e7' + \
         '2be15d0cc6a8df1c9bec3a839a4f851a1b43fdc91cfafddf5dea91a6cf7b7b01' + \
         '5ef0f3801e2948fe8657f24fe701a096999a05e84b924b08370fd235267b5374' + \
         '337c30247de5dfd39991414c24fe575342d80d1a2d08c36399f62e61d7af5fba' + \
         '5aaf9b122218657a469ff39c61d503b469d3c97f9337f16656721d7d5e91584e' + \
         '17027c3e68ea8b8d7ed88baa18b07c911a4c19f1f4981048bea9548e04b02f30' + \
         '5a09afec6d57d5ce406ecc345c47da985e85daef490ba35e41a1755352f10b51' + \
         'f71e47deaf1338d862ca4ef4a2cf4bac22f3a0b790f5344a73f6b9b8d6d611c2' + \
         '4231c27a288439de571c03a08daa750b7767342e935f73fad6cd9dd1e6c8ed5e' + \
         '80328051014692d9fc68e6615b75ac9357b5d2f9102db23a6c977bca6db90f09' + \
         '6c5fd53606fc91cfba3f2ce711cc81023c6a76c1e87e857b7ca872e93c8c7de3' + \
         '1a89a149cd271a19185f31d1abfcd81d87a4fcaed7aebf0676538f6f00000007' + \
         'dad9d25c27ff89ffe2dd8d2b546286a42d13949e2f725d154896d82238b04feb' + \
         '8bc3299eaa6421245ac8ced4a4a982be81522d5f4b5be5c9e2e0c50b8beaf78f' + \
         'bc7533ba89ada55488247e5cab2648c48163c2e5be7b655de12963ec9c2fdd1b' + \
         '90de8ed3c8a506f2b2526ed1e94c99834c1a288c7ef82e4fbb78f2cef5223c7c' + \
         'cecb9ae99f8b16fc104b259dfd147390eaaab623a21503706ee05adc097970a9' + \
         '12a038586f91df535894074a3294a6dc684759f0da9cc1bd1c441bcaf8113db2' + \
         '93e3fb1e5a774545b5f490ab6e423c4cd647594690abe10a317a3f81f278eed7' + \
         '103846b9114226dfc1bd87ff322c09f9d795cd92d52afd7d1758973264c3919f' + \
         '78ed2eaf0ebb6a5a1c666fb4c1c832a21591d4337463333440e9a4b1b618b645' + \
         '2bfdb6912ba266b6b9fceaf3674060321c82f219802959e40d87a42467bb7b5f' + \
         '3a182bed49f985156cfb9f69a43ea6f7f26f9127db64f8a4ee3a066c5e080a2b' + \
         'a6e4fb7357d54c71b3046840fd3cb4106493ab63c7749ee7ed605e8c7e7adeff' + \
         '55c7d180ccfba10b348d9c79a05f6f710cf16d9033a11b543d128afdc5421d2f' + \
         'cd6c871825ce19d88e71ae5682f801f6ef91b88da9e7cd424e2e1404652538e3' + \
         '39a4893667aac02fa273a79713407c5306a14785c78d5a51bbe4ee994f779fc3' + \
         '0000000600000004e9bd2ee63bc56b54455cda15bc70f95726fee498f23472e5' + \
         'ae6896b9d947946898e9a1e2d1f8575b53bc4724df0461780000000000000004' + \
         '82e653986041d9dbf52604bfceae1243858ba37e178c36cdb6d2b3921e1a44d5' + \
         'b217ebb12c4da84908425a66fa37be8d3c49b3a8280c16d2c097e0e4371d2876' + \
         '19f5168df75f0cf1a554bd1795b9248e049fd54f0f2205ad3511e64fc303d646' + \
         '03286d4a760e1a28d57e11f61fc058a93374db06334a3e2f8c8b63a4e30a508d' + \
         '0ed19e45248c206165358bb6a9744728c2ee38586ed1aba597b0bff8a749a71b' + \
         '98ca8b679725146a39323d7ac321c556fae2e5a9ae90a59fc19883d356d83517' + \
         'ca1e9841fec0c8a91a15b0375ac4c32931ae6a6a2044afccfd1a89fc5fbab254' + \
         '26c088a99a2163856d074a65ce6015d80c3603af83a6841b771d46b9a5b60b12' + \
         '3a35e8e3b2642351bf0b53aa80b3c7abc9caf0907f468439aa5e48e797195fb8' + \
         '22e0c4bd6adda633b82e28973ce2b2064e53bda8c9feb4182d09f83a3df04834' + \
         'e3eac43fd6b2e9e7fc0f6bf2d9c39afac6977c357ec766993d814b09215b8b06' + \
         '2c9d233fe956bf2eaa89f607d10d8211b1be4771daa15d19b2b68b5290b9185e' + \
         '65cc62e32c65bb78c6fdf89dc9e16199401ab11c755f5182064f6f9a89733e33' + \
         '39c398a2cdcc35b6062db2c7d02acd3f85549828a523043d2a6425291f30d3d6' + \
         '6d4a4510f2692adee82b010b58d1471c4999bad7a125cc3f97d0694c2e7bc422' + \
         '338581ea6c7cc4913e354fb0b40af34889b84f996ac23f3704d45def4df49325' + \
         'a0a84b1cb1d58312c301ded6a7ebc4ffab4bd26ae191970ebaccce0dffa78013' + \
         '87b77f3d8eb41ad61eb7b7cb6319c51dc982ec6281c74641517a82b178264b4d' + \
         '5f24f8ddc59562b4a9bbcbfd74b244ecdef6cfaaa68b83ddee9a964bb97cabe0' + \
         '815bd6487b68e1ad636f69f8af1bad9a632cf104718c9722d81260a67898e2c7' + \
         '08a31f1b8f891b41c0c906cebdebd2885c3b41bbc3089e036f6bc1ded2ea6d93' + \
         'a1f515d217f89fc20a3ee59940709f41452351bbfef6567ff6d1ec6eb0079f8f' + \
         'b9308ff891e2990603874dc0629802cdd390dfb668ea1f0e76271b7dde6e0538' + \
         'ee9390f9a62a75ad975d62466182698713fef33574941b898be07710503100be' + \
         '6fdd58cbfce444ad6cdfa96b9de6a8aa539c970e7210770d01e2f20e62567cbf' + \
         '2cf8e130062118e2b01e9dd67adca43e436bd00009f837fb8a43d8c307045d90' + \
         '3e3bf92146c6a11588cc3b86eccae91990fbdbfe4fe37b8a729e86340d0adc9d' + \
         '8629a6859ac8b8faf6ece2d6b3e5c16b40ab1638e51c5e0ef50e21b69a6b34eb' + \
         '473849f1417a0a2e2e7c766c714b25e6127c88bd7ebd72a35195970432ef6bd9' + \
         '5f1f7d41c1be93513ee35f663cd7fb63f6b40c1b19c536ae15b6cd9bdfcb10f4' + \
         'd069b17b0c56bfad5b7e5527816688a360f5024e3b92c5cfe6f16c5769ca3b10' + \
         'a65dd21f6a3a103402f28bf329b051dc47b6ea884b40c6fdb6deb25f456a0a70' + \
         '36295a6960b678103fd59f1b24b24295c030e9d08863eb579322f58f9f5e8063' + \
         '1ea9421d8cc30cbfc0cf66a624dc46907a1c689f6aa48b88da65ed917c40a5e4' + \
         '41c74265f5228295ff4e70432b2e8d3023e2ff31b568d6f56872e078ab46b260' + \
         '00000006dff428e18ad4ac9d392531f1fa73b5c62c84d850c92b8ba2fc81c2f3' + \
         'ad9a5ff6f183895fa672ca2c9a33672c74fa06b60116287599450624865bb59b' + \
         'ec5cd6ca705df7cb1a82f706176ea999ceaa69f1ed1e863bbea0a2253de93221' + \
         '13e6a6640c9d4bf91434cde1ea8987218c30b0b74542dbdc10c5630aad162b6c' + \
         '6f6d04119317b0e74a0a31ec2fbd2fe3c34db484722d75413d2ba8d61f7bf35c' + \
         'e80c80cd56ef5491e011a366f5219bd6d966c6c4715cee7d7356924d30d8b33b' + \
         'b308c3b9362d37a59a9924031dbda583ecfca3555727cbad2722ff79fd1f35bd' + \
         '856f43c7bf9526d641d6b5198e2e70266053b0094a71c97b70c356a85fafc3cf' + \
         '00123e1eebc69dae50b29c7ae19614fbfb018ad9e55c8cc61943b308d2605a69' + \
         '414b6e6c3d8daf52943caab3e358eaf0d5e8262b5df0b8552ee5e0be27abfcad' + \
         'e60dfe0a')
        pub = pyhsslms.HssPublicKey.deserialize(pubbuffer)
        self.assertTrue(pub.prettyPrint())
        sig = pyhsslms.HssSignature.deserialize(sigbuffer)
        self.assertTrue(sig.prettyPrint())
        self.assertTrue(pub.verify(msg, sigbuffer))
        self.assertFalse(pub.verify(msg, mangle(sigbuffer)))
        self.assertFalse(pub.verify(mangle(msg), sigbuffer))

    def testVerifyCryptechLMS5LMOTS4(self):
        msg = fromHex('496e2074686520656c6465722064617973206f662041' + \
         '72740a20204275696c646572732077726f756768742077697468206772656174' + \
         '65737420636172650a45616368206d696e75746520616e6420756e7365656e20' + \
         '706172743b0a2020466f722074686520676f6473207365652065766572797768' + \
         '6572652e0a092d2048656e72792057616473776f727468204c6f6e6766656c6c' + \
         '6f770a')
        pubbuffer = fromHex('000000010000000500000004252f23eb390448e6bb27' + \
         '39d0dea7c26c19585e92cd428ba898cdbfaa0843e479dc8a0ed6539fbcf5475b' + \
         'c83f28f6e071')
        sigbuffer = fromHex('000000000000000000000004b555fe1dd483c70ce769' + \
         '05ead00e17607598369bd276fb9113a8ed8bccffd0862eee3ea17a2fc0017a1e' + \
         '46d57bf6ed4187b2c63a93dc4bb6c56343e5369c337a62d048ace6a26dfad23b' + \
         '2a714a1a90c4f0a6a0175a5d3f2b3235e18550f0e4c49b6fa6988ea4920f4220' + \
         '55dc196c57d909254d3d2156f6ff338e3a8c0a564f47722d3aec88401eba0628' + \
         '2663a5af7d88eec4a44afe891c54a8b9ed0f5fab9eff410fcaf8a3ad9e5410d6' + \
         '33862349515139410e3b0e62000ce8d0d82ca9e7bb7480af71f6b61f13e717f6' + \
         '995623acf9145ef65fcc2d0673e05c4df050dce485570099a116224d005b9cd4' + \
         '99ac34ee20ef0516f6496b8193d9bf0abcca9e6fab44ace5ae04b6ecbb3ebdf2' + \
         '79d0aa489b097869e42cb020e58e9b2077d1dc17fa5008aa346a0b4861e2f464' + \
         'c2f525baa53b3b13913bdcb2467da6ce744cd3ce527f515d5ebf9529d097ee9b' + \
         '2988af7830c0df01f4a843d327536f68e3c80819dce5fa58a5c54e2b1ee5edb8' + \
         '4de965b28af2439bf4442552cfab8b5891b59739fe3fa75de9dc8664b1ac066a' + \
         '26cb69d0f5b607597737c2a1e3eec1a982e745476e81f8c3a8c3cec09592fd04' + \
         'd07f2ae2639b07240f3fbc1738940d33e1fc9314b09c2af7910b50f5f76d6325' + \
         '471b8c836b190ffaf8f3ddb6abab81398a16575177a60959ab1522b775654a2b' + \
         '7a9a56c206a2030da9034ce908d02744f0b69c1291603e50b6afc65dc30f2307' + \
         'e3ed7886421eb24f2bf0722203a6bd33d901c0a04588c25f185d586e3689f0cf' + \
         'c265fa9aa39212b2435351fa1fcea26d8f14990f9d6b87953ad6dc4d07ad122c' + \
         '73cd91c41bc9fa7ce2cb0c8b7eb8044beb298da332a65a27fd304474605bed41' + \
         '65211c5ddb92ad127398bf9f975268d0299f0b3bc48fd14861b827705e5a997b' + \
         '8cd922989bd13fb74ed1196984cde8185678431ebc5e9c9e87a1fafe798ba9d6' + \
         '431779171de1a2ea1fd8cd118759afa3a6c35661913e9f209ec6f8860e82a8e2' + \
         'b9c4f2b759255f6b417907d9dc74c34155432cd3a52755ed6c4354b2e7e83fad' + \
         '5edf7427ad1ea2f9cf10109cf6347f94b913ac4e7d5d1fd8191a20460a9ef438' + \
         '0a58ee5beafd9653b575c70f06a5c961470e2a0844f11e237d25232204772732' + \
         '0684df25944a66c6dee3625c5eb6c3990ba4da029c8f5b17f74c5441f26b6279' + \
         '2f3e2057a92207360023c544e90ab01e01e12022a9a86a11806268e75d258bc8' + \
         'b8d2423e661b366be4a726b614ebdd300da9329436e90a44c7e59a360474d0bb' + \
         '99b16222b77f754f2a7cd310acabdfe82d4bb9d3998f0ed2d0b2cfa0948ed7d0' + \
         '8b5ab8e9ab132f4b0e90c83f112e5e37719132c944cda3089eb53f2825edbe81' + \
         'a30fce872b802d71be97013d26c32a89e6f911df0c7abcb67196a05c95ab2f1f' + \
         '02188d214f487334a4310563818831c36202c0248c789e5b9328109af0b7cc72' + \
         'af610c85f988b492821aabd5ed68b8495ac4baca394896c2ce2180cc5fbf9ebb' + \
         'a392a405b827b799cf011f0b684f2c3783836dc44ed6d6557d6a3bcd2df3d0c6' + \
         '69c7e823a96794db240596299f3635997ffcabb9e9c2000000050d3097937263' + \
         '943036a78ddd20c9a93feac4bd74094f9026356c3bc4aa53a5f5d9cf33adacc0' + \
         '8230f978fbe798dca261e84c7415bd7dc183595be9f7d2736ba578597e04b7a0' + \
         '1d74755ff18b9a0c2168d820cf5c9d2399e0713515bc5836d4460fae1a86a27a' + \
         'dc43b29f94cd809c94290efe9071430ff6ce3eb8ccf332d32b3688015072376e' + \
         '3df28d4dad3d80ed3cfb32a8a4bfbc56436a4dcfddd28ed3dca4')
        pub = pyhsslms.HssPublicKey.deserialize(pubbuffer)
        self.assertTrue(pub.prettyPrint())
        sig = pyhsslms.HssSignature.deserialize(sigbuffer)
        self.assertTrue(sig.prettyPrint())
        self.assertTrue(pub.verify(msg, sigbuffer))
        self.assertFalse(pub.verify(msg, mangle(sigbuffer)))
        self.assertFalse(pub.verify(mangle(msg), sigbuffer))

    def testVerifyCryptechLMS5LMOTS3(self):
        msg = fromHex('496c2073656d626c6520717565206c61207065726665' + \
         '6374696f6e20736f69742061747465696e7465206e6f6e207175616e6420696c' + \
         '206e2779206120706c75730a7269656e20c3a020616a6f757465722c206d6169' + \
         '73207175616e6420696c206e2779206120706c7573207269656e20c3a0207265' + \
         '7472616e636865722e0a092d20416e746f696e65206465205361696e742d4578' + \
         '75706572790a')
        pubbuffer = fromHex('000000020000000500000003c03bc9f29edd47c497cc' + \
         '136c258a3c9c8c9c6a1a79cf69fe0ab8e99327c536b43fd0876319c31988c943' + \
         'ebb6aeb97a11')
        sigbuffer = fromHex('00000001000000000000000333b2eef16b9598470c9d' + \
         '4612090b60ef997b20c16ce3501a62ea65ed8a31e3cd4e99098e7840e8cfb450' + \
         'b15817eb564c0395047f5c65e68ee7a4e440bb67a8bd654c3d984a4787aa0309' + \
         'd9e6ecde7a98ff57ee126c82d11d288caf619f7886f6b878bc1fa8efc11ae30d' + \
         '9e01c158a792fdf08768a98d163e9ab180eae8e46f69988c7e78ef421fbdc2ba' + \
         'd01b2623c0c557a0ca9816c1b76721590f2d39ded59edf780e3b9038499e7e3b' + \
         '40d35009b30a795d924f6bd0d602071f5873fdf6f7f0c1d8f046222f88b25168' + \
         '67254c6d8a2d148f36f05d7ca5ee6b20bc1011c5d33372d1a806d55a53733480' + \
         'ade434c195787269e20da87006da772d0d0079f50c0dc2676cc14e78109fa8de' + \
         '459b408e53be21bddc23f8bed95c86ec3ab348a5ae7fb484cd5397adeebc1324' + \
         'adab443d79c7b39aaa915536d3f2e3f0d7ae4ab3332605b9ae858509fbb1ada4' + \
         '64d84f1c5a26c99181d9587795c33563d55094e813d56cb58d9b20216ff43c58' + \
         '6a99e20eed3442407dcd59f7892d1b0545847bfa73503edadf17a517dafed839' + \
         '874adf8f4df3e8dda0863c9e6df9eeffb9097ccb27ea5929ce29087d523f285e' + \
         '0af8645012658fe06c8f0abc48a73cb19c0701a8ee1ef190a72b3fba90b3a636' + \
         'cf3edcfde978e378499f89a53df8984e8c760f6643ee7d18e63e3c80120d4a6a' + \
         '56c3a55100adf2384334b06530999fa94192e97184068cefbbe519b68198bcb9' + \
         '13ae2e5c5f2db2913dc3b881dda60ab2bd06d09074f230439e40be01ce080466' + \
         '6300ad7bfe72a43f18d50fdf2fec8c4fff2324a7502bb3e3614656ed5bc697f9' + \
         '72d5233c4fba2a81e7eede74cf109f1e0f7870e15f55da2fa200a874cf2d9952' + \
         '468b52d1bbf71889062d3a7a8753eef1e7b7b451d963f143c52d3193dafe6e7d' + \
         'eccb98e25b98c0e2ceb1a5eadac896108ece2cedcbca60e21fd00ee1d4b2e4ea' + \
         'd3df585c44b37809c0516133a644780702d4938a64630d5e8e4827dc70d2bbf2' + \
         '37f5dc46c50f38b5b3ca8d9ae4f676ce0755967d9ce5ce87abd017ac53409ff2' + \
         '318cc91c34e0a37ac810591262f7e7c29062e49b296c65594277723f38059fda' + \
         '499487e9233dfef2c1c70267a297a68ed3ab26af4ee73d155f23d56309359f75' + \
         '6e45697703db2e6172fa7c299e595c653df1ae360db5c3f5dbc73ed0ddfce960' + \
         'faec77d7aee8134965540789b4aefd32feb293854ef078a727afdece8247e900' + \
         '2c26436bafc9d5d5729dd933a5eaafb0f03c29f858715ae922149cd2c9e95351' + \
         'fa5483b74c203820e4f9991237df02a1d547f4944ac8039e11073e34716442ea' + \
         '1127712c084da05e4caeb0a11b73230841b83a89a749eeeedd825bdc0357d831' + \
         'fc57becfd79b49d41ff1e691a67c574ae5c1451b79d084441d4aa38c3e2f3ea9' + \
         'a215393175ba318170be62c3bd604bd9e0ab787189f29845d1f888e2db45d1b4' + \
         'ba758df3255b895b378dc235146720f73f65ddc1898f176b96bb93010d74567a' + \
         '79f042dd3e81080788fd4094b7c33e88de46c78f0eaa64ad7dccab3996b82340' + \
         'fc1f40d5f8e44c4ecda729fc11e8a7e1f8e25af8fe1a226b92d1108dfefd4928' + \
         'be2e37c6cbbf19a4f4e418eb89eb3e8a6cd629fe1e4eb87e9c1eebc148f58aa2' + \
         'd36dc539610765b5a4ad82c078c1f165ad63f208e53aaaa0f06a9fd52d2eac60' + \
         'f1fdc07c614b941fd4d643546c57c42e92385a6725c9da30e1237d184a6c87e0' + \
         '2d3eac0aec9046693fe9be312158ae9dcad1e0b9c7582e6fc3ffd430f8c43b36' + \
         '5d214454797cd7125201c2e705721e02f1a7c8b6cfbea7dec05fd2e62ebc340f' + \
         '5d654a644defe9cea45e2838de0f9c861cc7b3a9ed878aee2310ed25fc6273a1' + \
         'bf660fd2687546cd0e0bf9ee36f897bff1af3828c348af33fa6a3613c983b7f7' + \
         'a2cec4e045e7560626410f9937ad90a7358065881275e77c922772ed3aee4427' + \
         'a9c239476c338f775ca6fbe0b3d625c3e682cd15c3449ea37556c071822358bd' + \
         'a86165e3a7c38f4a41af1db75e8bf60027935526d0f2d9ab21b5da682f0b1bc8' + \
         '5d3516f1e0f9e586df153d86300a6ccfa7226bde26c625d94c09c6cf539e8a9c' + \
         '5dd653ec1ea92a9c4d4feca14bccae7f3c27037f4339ab582562b51ede9c2880' + \
         '52cab12549206624f14c34d2c9123ff82b2b6bb13115936f26d7fe741ee2ae20' + \
         'a6c8b8363b7a6c6d6af8bfa97d20230473271b0792890813633e48ef2dede6a9' + \
         '8110c02669615983999a7922dd36b57966055a6b42abb071e6079dab67a58989' + \
         'cb001b61d1569992c6a3b110c13d45da678c3969b0daa1a57d766695d7d3c064' + \
         '780381c85c96ce0a771aacd3d9bfb150bf6d5693da2366e49f3a243cf0828f89' + \
         'c5fae261e4a84bdd29a3f6b66c81adaacf861a57fdbb8d4131e17d23a926872a' + \
         '0f454ffc8440a96a78106f805dd966de41ec5c5d3e3124fe934e21ee715a887a' + \
         'cb14ae5d9c3e7717f5418f8f71c262189ad08f895832df42279392768fe9c123' + \
         '3bf184ad7c25762f2f51bf84ac5a52c96847176a2fed91c936228589fb9d6473' + \
         '67920f7904f63c481e5a617dd1e1635b8f6d087b6e4a9360cff1d0fe71f45e10' + \
         'ea01440b53cede5833851ab01da2a37063629e831eb08ac7d45989ebfc6d9b6c' + \
         'bdcb8c85f1255653d301c8cfd2ab2cfcd772426f7ca4f2f094fdbe743d7e4d5e' + \
         'f14c3392f252c897c79991e97f2cbe82dee67c5e1c14eee248a597b68b0a8bce' + \
         'acf513d1a4f9262e798063786130a49d48b9b0940640e8ffe1940afccb03a07c' + \
         'ec10445455f6ef41d1970a656f77c84cfa9e067a61338bd6819bb60a6ab955a7' + \
         '3d939b6773e6877ce1cd91119b8c6468fc09ad5d3d4344c8384be5b91eff6116' + \
         '5579bc1739a0b26be5dbf7e9b7850563304618a5c57ae2ae2443a805e2992af7' + \
         '16c273ceecb8dbcbf10f716f5afc221d6c2455a38a8a046cc8e8405a7cd55101' + \
         '9ef5889a042e09e2dbd5f771fe025f79bc596df54a73c3d7b46863fcb6c5bfbd' + \
         '937fd256b2a167896bea518dfe601fb38967a3323399949690af4d44958796c2' + \
         '2ca60f5095a2c443bc88a31b3e5c3a3c750c246f8fd90000000579f88118bcdc' + \
         '34431f15a8b630504eadd7fd1a2260997e3c413258b4ed85da96807b3b068482' + \
         '3567815312eabef25358d756b69f15d2a8630dae2ec73281113efbe11c8110dd' + \
         '416eb1090ad6b65693991829b472ce2bbd283f3254dccc64da67ec2a221aebca' + \
         '9d78e3b0007a89e97b9ea1a7fbc1769a3c6296ca07e93c74422a9963fda1dfa2' + \
         '3e4a4a1a20452d9da1ca50e3ac03fa21c50a75cfaef1faeda056000000050000' + \
         '0003c63549df46f94d1bb0dafb337aa176bcad04d3a2d7e9dd79b7e6237b5d05' + \
         'ff983a5bcb18e32a6de1d1fcdfb2a25142c100000000000000030da336e94bbc' + \
         'a4e836a4fac2e8974d178a2fa934c70762c3d9d8953dc09ae730cf60cd79e401' + \
         'd59111b9d27dea0363419893a77031222b3b9fee5acf5201d896d3a6c2b10d67' + \
         'd4e771036e5f8d89336762f5fb4e22decebfde67491af931561b7c16e6c28143' + \
         '30fe16839a915daaf8d521e41a1b0bbd43dd621b793fa982f5830e3249400632' + \
         '6773ea9ba5e0c1cd56322011f57adae278f3e4369cb01f1f900309404655f8d6' + \
         'b894afda905a2f5e4fcb406ef32d4eb3cdeee95116cf5e692dacb762491ed309' + \
         'ce6dc5d91e466af5ebe7086c6573d82f1531fec90ac05df454507a6de0e83cd0' + \
         '0cdc08ab1cedfe82a942f48529619556f8638ded2b1dd6bc16a96126bfbc766c' + \
         '79164f199f1494b7d98dcd2d6ecf9ce5134005fc1a1d984ff7702a0f0859cdb1' + \
         'df91871a750fdb24bf7cd87d031f299ffde038fa672ce8e80fc404a55cb56f3b' + \
         'b7898d62b8eb6e4870c95307f00d5c65a6b5122f58313ac4796ffe743585b2b6' + \
         '1f2a0a4206616118adc5810adcbc50e3e1f0fdff3bd748d433751eb43862df3a' + \
         'cd06d0716c940ad6e558dbc5bbd32617040e957bef267c3c34349f7c27f66408' + \
         '0388f6dcbe97c7689634438b87b0e30b84b0e7b55a697f4d1582ddf1078c3b18' + \
         '7b6010f115ffa14669b810b6d7040c243596c53e861c612d97f9d309bbfdfd0d' + \
         '635982b57e038b83a7ec376289b92826a8771b105b7f97ed49d55b77ff16ee44' + \
         '48cdc2176aea67075e5376dd9b25dfddad898699d2ece95bc61c717706ac3ff4' + \
         '0dd060137d1fabdf608f30befc797ebf71720497ec9a709a8325ecefb5e6f708' + \
         '010f03dd8c416d0c28b6e23625c1b675400ed34b69f43b6d26b9c2823ef6b727' + \
         '861b183032a5ef4d7f720aaeb2630f8957fe61814f8a752a0c429e8c8c9022a9' + \
         'f677ee2b799985f89dd311f904c17f21b8059d83e403f020b8ba98b04c195edc' + \
         '5cdadd3fb2f0dbf7fd6ece1a65b2f18f37c3d1340a807508c5e5bda9e6c60bc8' + \
         'fd3889f640eb8a9244902584570ace9fd0433c5efd2121c34f4ecd89eb020e03' + \
         '3a33dde3eb3c8b199560131459411379c4fcd2adf8f77d89c6727b35382d70e9' + \
         'cc8dc0b1a65cadbe559763c3f3bf9351ca749a7670e6d7f4f9850a584a78b4ed' + \
         '506a7a86ae650b301bd1feaa0f9d1221935e0f018cb8b2cd5ca4065bd732bda5' + \
         'e2a267e7736c87dc195b1eac50273ced1a8845d82b2024b782e2d5a310726ee4' + \
         'b6dc629c2ddc9c74a3568f33bdd731d4b6107dad07189eaee0a4ff550fdd9ca0' + \
         'da5778373856785ed0fcb10adcb6b1a631dda0d5a2eecb59d5deefb7e7007c01' + \
         '0f3009f399be1efe5f4bc924d327bcd3532e13ad2e43a1c737a28f378b9e5bf4' + \
         '81dd412689b7b313d2e3bf2ff2b78a7870e9914faeb45988a67955abfbda3e2f' + \
         '2d7c0b0cb257f9c13feb4989decf42d4480b468d18d7b2a921af14f354869fbc' + \
         'd05d63fae15de91ade383b506c7d974839e74f8783d38780b1ece3e7e08c222c' + \
         'ebc73dbce655cc2831d4e4e606ab965bb080613465dad3fbb16e827c1caadb3d' + \
         '26f1590c138ff21a080e9dc719daa990a072ed7b9aa494e3686381aa42b697d4' + \
         '2a033f0ad2cd0b79e5ea51681c225f13a2de9b89f6da99398b703ffc5b347317' + \
         '341e9f0aa47cf0ea495b9f2c1dc10c4ce243842b09e0dc1f0ea3363cd2d1921f' + \
         '000ff088e548b75a432595246ca66c06ccc95b9945f831bcc43e2fc7bb302006' + \
         '4b380ebb75bec3438be2b4300149c924f579692c397f0c20146d63a4acdb8ae2' + \
         '6eda44f0372d6cb2751dcaf05510a89a901b05c321e8faae428e38d1cfd0bc0e' + \
         'cd227c57aa8e22b2a87e801b0d189ab9c3624898ce3fed895cc99fcebbcdad76' + \
         'bb205b6e9879d8f5792b8619392f25e8f951548ce7b4fea562d8ceacbd38da62' + \
         '9654ae27a966ef6c6a6a0b91e9c6455d6ae45810cf250f60c4c8919bdff56f00' + \
         '8b535b8b932e2890b7252b53bb05fa205cd2850416a7aae97b16b10c86b46724' + \
         '0d054ee3d3f601a8f8d17d2b4db4e76452eee921cd6ebca350dd9b254737346f' + \
         'b67808f01fe206d1e473b055bd87d043e515d18262dcd29edcde34d8987c9d52' + \
         'edd05fa53b0eeae15bb052b9602e05feffed69e8a5c120c33c7d4f5140361688' + \
         '10ddfc837c815fa46fe6601be20fe1d643c1bb8421f624bcabb9124f1753f5aa' + \
         '180b648a90a3c45661cd570c2d2f4698e73b2b383d2525939a0ffdbb8c201bdc' + \
         '63997b8dd5e23c73e32f747b51d157670b9143155265c37e7a2b942c8f661ba9' + \
         '283d5309b2016382f1e6fd36740273445a85f5e8e0186229cde37bfebdec2e6a' + \
         'a38019eaf06401149fc4634c63f64fe0889784adaa7333254a6c8ccd26808b23' + \
         'da0381f9b51521b56ec64f36c7a5dd3336e135bafa7f982f0ad01eba2e9a9928' + \
         '1aaf73b53fdcfe3f0022f7e08c439a3e09f8aafec1a645b181492a6ca76302a1' + \
         '70813ef0d55537c08d4f0819985319c62d160870cb9b51d27f8cc5c23edf1dc3' + \
         '896181640bc03658a168676df3112600a845f546f17c4124af93e936bd5fa35f' + \
         '152666d3ec6c2c52bbf9d71fb779f639090932fab4f41a0feceeff1e19232da4' + \
         '3d409e2b516bc490601d8d23b5135bf7142ea3af65890c7969e3a6a8061e9a5c' + \
         '2146d20c20e838e90fc4090bed0d3a859c7e5d808ba59637f1976a474d6f3eef' + \
         '9fb9da3d1375073157909dc05dcf99b5be63c32227a1273928dbb0fc6c396790' + \
         'd78f3796b4a7c64bd5f4ae6cf107b9e8efa4839c462f6305143d4072389eff55' + \
         'e410d44fd50397ec44820585b4388b08cff6af4c5417e32072724256562e8aae' + \
         'f5da77b085af4ef6c7bdc5705edfadee134eccf1838c03574720c487501bcfd6' + \
         '83bb0dd52404dadf879dd77fd0b40dd3237ee83854ef817359e24db6edd72922' + \
         '946c518bde26d2aec51a136d027b9eecd12911f1ec0847d7f3c865f05d1f3f84' + \
         'a72cb8f2014153e77582698b8563fa4a7f88db7c76bfbe2760a2a1399d5083b3' + \
         '4f1077025cd0a075e99acc9fe19a96cb92e0b2d71efb5149a5478489d3fe4ad4' + \
         'd0d40971216f266b3b2357c06c906b2ae6ee3eecea3537c3a775000000050d68' + \
         '9fe64b6dad8a84803efd298f688d169d318e7dca25c42d50c00296cf53e897bc' + \
         '3d523cf3b8c8892d83c78da74dcc330b8534e53d922ce0ba1d4a9f0a14b5f428' + \
         '36ba9d191995cf485136805c41c4eb2821e48a42a5f7ce32fcaffb40c984b895' + \
         'b99cf60fd49133729e46a12fd6824c02f59413d4dea9085003527081e39416f8' + \
         'b935863df45990a385f5c437fcb745307e3046f5f1b6b10e6ea02262116a')
        pub = pyhsslms.HssPublicKey.deserialize(pubbuffer)
        self.assertTrue(pub.prettyPrint())
        sig = pyhsslms.HssSignature.deserialize(sigbuffer)
        self.assertTrue(sig.prettyPrint())
        self.assertTrue(pub.verify(msg, sigbuffer))
        self.assertFalse(pub.verify(msg, mangle(sigbuffer)))
        self.assertFalse(pub.verify(mangle(msg), sigbuffer))

    def testVerifyRFCExample(self):
        msg = fromHex('54686520706f77657273206e6f742064656c656761' + \
         '74656420746f2074686520556e69746564205374617465732062792074686520' + \
         '436f6e737469747574696f6e2c206e6f722070726f6869626974656420627920' + \
         '697420746f20746865205374617465732c206172652072657365727665642074' + \
         '6f207468652053746174657320726573706563746976656c792c206f7220746f' + \
         '207468652070656f706c652e0a')
        pubbuffer = fromHex('000000020000000500000004' + \
         '61a5d57d37f5e46bfb7520806b07a1b850650e3b31fe4a773ea29a07f09cf2ea' + \
         '30e579f0df58ef8e298da0434cb2b878')
        sigbuffer = fromHex('000000010000000500000004' + \
         'd32b56671d7eb98833c49b433c272586bc4a1c8a8970528ffa04b966f9426eb9' + \
         '965a25bfd37f196b9073f3d4a232feb69128ec45146f86292f9dff9610a7bf95' + \
         'a64c7f60f6261a62043f86c70324b7707f5b4a8a6e19c114c7be866d488778a0' + \
         'e05fd5c6509a6e61d559cf1a77a970de927d60c70d3de31a7fa0100994e162a2' + \
         '582e8ff1b10cd99d4e8e413ef469559f7d7ed12c838342f9b9c96b83a4943d16' + \
         '81d84b15357ff48ca579f19f5e71f18466f2bbef4bf660c2518eb20de2f66e3b' + \
         '14784269d7d876f5d35d3fbfc7039a462c716bb9f6891a7f41ad133e9e1f6d95' + \
         '60b960e7777c52f060492f2d7c660e1471e07e72655562035abc9a701b473ecb' + \
         'c3943c6b9c4f2405a3cb8bf8a691ca51d3f6ad2f428bab6f3a30f55dd9625563' + \
         'f0a75ee390e385e3ae0b906961ecf41ae073a0590c2eb6204f44831c26dd768c' + \
         '35b167b28ce8dc988a3748255230cef99ebf14e730632f27414489808afab1d1' + \
         'e783ed04516de012498682212b07810579b250365941bcc98142da13609e9768' + \
         'aaf65de7620dabec29eb82a17fde35af15ad238c73f81bdb8dec2fc0e7f93270' + \
         '1099762b37f43c4a3c20010a3d72e2f606be108d310e639f09ce7286800d9ef8' + \
         'a1a40281cc5a7ea98d2adc7c7400c2fe5a101552df4e3cccfd0cbf2ddf5dc677' + \
         '9cbbc68fee0c3efe4ec22b83a2caa3e48e0809a0a750b73ccdcf3c79e6580c15' + \
         '4f8a58f7f24335eec5c5eb5e0cf01dcf4439424095fceb077f66ded5bec73b27' + \
         'c5b9f64a2a9af2f07c05e99e5cf80f00252e39db32f6c19674f190c9fbc506d8' + \
         '26857713afd2ca6bb85cd8c107347552f30575a5417816ab4db3f603f2df56fb' + \
         'c413e7d0acd8bdd81352b2471fc1bc4f1ef296fea1220403466b1afe78b94f7e' + \
         'cf7cc62fb92be14f18c2192384ebceaf8801afdf947f698ce9c6ceb696ed70e9' + \
         'e87b0144417e8d7baf25eb5f70f09f016fc925b4db048ab8d8cb2a661ce3b57a' + \
         'da67571f5dd546fc22cb1f97e0ebd1a65926b1234fd04f171cf469c76b884cf3' + \
         '115cce6f792cc84e36da58960c5f1d760f32c12faef477e94c92eb75625b6a37' + \
         '1efc72d60ca5e908b3a7dd69fef0249150e3eebdfed39cbdc3ce9704882a2072' + \
         'c75e13527b7a581a556168783dc1e97545e31865ddc46b3c957835da252bb732' + \
         '8d3ee2062445dfb85ef8c35f8e1f3371af34023cef626e0af1e0bc017351aae2' + \
         'ab8f5c612ead0b729a1d059d02bfe18efa971b7300e882360a93b025ff97e9e0' + \
         'eec0f3f3f13039a17f88b0cf808f488431606cb13f9241f40f44e537d302c64a' + \
         '4f1f4ab949b9feefadcb71ab50ef27d6d6ca8510f150c85fb525bf25703df720' + \
         '9b6066f09c37280d59128d2f0f637c7d7d7fad4ed1c1ea04e628d221e3d8db77' + \
         'b7c878c9411cafc5071a34a00f4cf07738912753dfce48f07576f0d4f94f42c6' + \
         'd76f7ce973e9367095ba7e9a3649b7f461d9f9ac1332a4d1044c96aefee67676' + \
         '401b64457c54d65fef6500c59cdfb69af7b6dddfcb0f086278dd8ad0686078df' + \
         'b0f3f79cd893d314168648499898fbc0ced5f95b74e8ff14d735cdea968bee74' + \
         '00000005d8b8112f9200a5e50c4a262165bd342cd800b8496810bc716277435a' + \
         'c376728d129ac6eda839a6f357b5a04387c5ce97382a78f2a4372917eefcbf93' + \
         'f63bb59112f5dbe400bd49e4501e859f885bf0736e90a509b30a26bfac8c17b5' + \
         '991c157eb5971115aa39efd8d564a6b90282c3168af2d30ef89d51bf14654510' + \
         'a12b8a144cca1848cf7da59cc2b3d9d0692dd2a20ba3863480e25b1b85ee860c' + \
         '62bf51360000000500000004d2f14ff6346af964569f7d6cb880a1b66c500491' + \
         '7da6eafe4d9ef6c6407b3db0e5485b122d9ebe15cda93cfec582d7ab0000000a' + \
         '000000040703c491e7558b35011ece3592eaa5da4d918786771233e8353bc4f6' + \
         '2323185c95cae05b899e35dffd717054706209988ebfdf6e37960bb5c38d7657' + \
         'e8bffeef9bc042da4b4525650485c66d0ce19b317587c6ba4bffcc428e25d089' + \
         '31e72dfb6a120c5612344258b85efdb7db1db9e1865a73caf96557eb39ed3e3f' + \
         '426933ac9eeddb03a1d2374af7bf77185577456237f9de2d60113c23f846df26' + \
         'fa942008a698994c0827d90e86d43e0df7f4bfcdb09b86a373b98288b7094ad8' + \
         '1a0185ac100e4f2c5fc38c003c1ab6fea479eb2f5ebe48f584d7159b8ada0358' + \
         '6e65ad9c969f6aecbfe44cf356888a7b15a3ff074f771760b26f9c04884ee1fa' + \
         'a329fbf4e61af23aee7fa5d4d9a5dfcf43c4c26ce8aea2ce8a2990d7ba7b5710' + \
         '8b47dabfbeadb2b25b3cacc1ac0cef346cbb90fb044beee4fac2603a442bdf7e' + \
         '507243b7319c9944b1586e899d431c7f91bcccc8690dbf59b28386b2315f3d36' + \
         'ef2eaa3cf30b2b51f48b71b003dfb08249484201043f65f5a3ef6bbd61ddfee8' + \
         '1aca9ce60081262a00000480dcbc9a3da6fbef5c1c0a55e48a0e729f9184fcb1' + \
         '407c31529db268f6fe50032a363c9801306837fafabdf957fd97eafc80dbd165' + \
         'e435d0e2dfd836a28b354023924b6fb7e48bc0b3ed95eea64c2d402f4d734c8d' + \
         'c26f3ac591825daef01eae3c38e3328d00a77dc657034f287ccb0f0e1c9a7cbd' + \
         'c828f627205e4737b84b58376551d44c12c3c215c812a0970789c83de51d6ad7' + \
         '87271963327f0a5fbb6b5907dec02c9a90934af5a1c63b72c82653605d1dcce5' + \
         '1596b3c2b45696689f2eb382007497557692caac4d57b5de9f5569bc2ad0137f' + \
         'd47fb47e664fcb6db4971f5b3e07aceda9ac130e9f38182de994cff192ec0e82' + \
         'fd6d4cb7f3fe00812589b7a7ce515440456433016b84a59bec6619a1c6c0b37d' + \
         'd1450ed4f2d8b584410ceda8025f5d2d8dd0d2176fc1cf2cc06fa8c82bed4d94' + \
         '4e71339ece780fd025bd41ec34ebff9d4270a3224e019fcb444474d482fd2dbe' + \
         '75efb20389cc10cd600abb54c47ede93e08c114edb04117d714dc1d525e11bed' + \
         '8756192f929d15462b939ff3f52f2252da2ed64d8fae88818b1efa2c7b08c879' + \
         '4fb1b214aa233db3162833141ea4383f1a6f120be1db82ce3630b34291144631' + \
         '57a64e91234d475e2f79cbf05e4db6a9407d72c6bff7d1198b5c4d6aad2831db' + \
         '61274993715a0182c7dc8089e32c8531deed4f7431c07c02195eba2ef91efb56' + \
         '13c37af7ae0c066babc69369700e1dd26eddc0d216c781d56e4ce47e3303fa73' + \
         '007ff7b949ef23be2aa4dbf25206fe45c20dd888395b2526391a724996a44156' + \
         'beac808212858792bf8e74cba49dee5e8812e019da87454bff9e847ed83db07a' + \
         'f313743082f880a278f682c2bd0ad6887cb59f652e155987d61bbf6a88d36ee9' + \
         '3b6072e6656d9ccbaae3d655852e38deb3a2dcf8058dc9fb6f2ab3d3b3539eb7' + \
         '7b248a661091d05eb6e2f297774fe6053598457cc61908318de4b826f0fc86d4' + \
         'bb117d33e865aa805009cc2918d9c2f840c4da43a703ad9f5b5806163d716169' + \
         '6b5a0adc00000005d5c0d1bebb06048ed6fe2ef2c6cef305b3ed633941ebc8b3' + \
         'bec9738754cddd60e1920ada52f43d055b5031cee6192520d6a5115514851ce7' + \
         'fd448d4a39fae2ab2335b525f484e9b40d6a4a969394843bdcf6d14c48e8015e' + \
         '08ab92662c05c6e9f90b65a7a6201689999f32bfd368e5e3ec9cb70ac7b83990' + \
         '03f175c40885081a09ab3034911fe125631051df0408b3946b0bde790911e897' + \
         '8ba07dd56c73e7ee')
        pub = pyhsslms.HssPublicKey.deserialize(pubbuffer)
        self.assertTrue(pub.prettyPrint())
        sig = pyhsslms.HssSignature.deserialize(sigbuffer)
        self.assertTrue(sig.prettyPrint())
        self.assertTrue(pub.verify(msg, sigbuffer))
        self.assertFalse(pub.verify(msg, mangle(sigbuffer)))
        self.assertFalse(pub.verify(mangle(msg), sigbuffer))
