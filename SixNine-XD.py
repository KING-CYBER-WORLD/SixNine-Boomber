# Encoded By ASIF HOSSAIN
# Py3 Marshal+Zlib+B64 Encryption
# https://github.com/KING-CYBER-WORLD

import marshal, base64, zlib

exec(marshal.loads(zlib.decompress(base64.b64decode(b'eJy9F1twE9f16rErWX4/IRCSiwFjg2VJNgY/cKhsC1CwpATJNagfdKV7bS+WdsVKsmG/lA6TejLtABNoGAJN2pnSaZOPdsYf/cxnw5fc8Ydnv7D7U9qPbib54qvnrh42koG0JazuHJ1z7rnndc89e/fvaNvDFf+//YcZoU8QQcSUQNHCvylqMiNqumwuCRPzQxNCX5hKtAlVzFsq54k1agEZK62aedlKmOcI9yw3ygPXZszwz85UyNmZTWKr1CkiYic1H5uIg9QCrCP1ABtII8Am0gywhbQCbCPtADvILoC7yRsA95C9AN8k+wC+Rd4GiMl+gJ3kAMCD5BDALnIYYDfp+dgUrSFHKK+yuI4yGHWQXnKYOO+bo7WkrzATraM85YmLuO9bovXEU5xvICjaSO20ccHKfFYeQCToclMpBuqgNV/2P4S8fVHOXbSZNl9uKWdyYMGYUdpoIzmm1sN8o7EDjZ8iMvigagclUw2qsFFHa6tstNLWV2CjrazhOG2g9V+eeGgBSUvZSjtt//+sbGXuTw+MGhiqqkhTGPUMP2FEUOPiCSooqvMqmXPKKSrh+UwmlR5xuZaWlvpmhTiNyfJCX1xOuubptb60QMQrx4ez/7Ij5MAY7/2JZ3RgILl5//ebdz985YNZgL+ClWPJjZXfbKz8/NFnGyvXN1ZubKz8EijchQF+vbKx8hHwHt0A6tNH97/+4z/v/5mhhtyNR5+VHQVtRa0/jMOGncGkY/POzdc2HIbR/qTDsfmr5R3GnU+qEUhBBa/IruK/VKDKWsmNO7efdfRBiX9r8869KjO3twSqnbxVibxApNLqS7NyC2/5U/IEbxFlU8915kVCz/jqYIa2e1el8cV2d0hbtTMvFitn5wFzZ+fM7BTgtpQ8L3HPcef5QjtUTkV+ypVT5G8hGL+I9z2WVYhUWmRd4r98HI7S6cev8/izhmYY9iTxZCgYwdNhHz4dOo8n/eHI9Plxf/CMc/Pe5//+yw3mIy51U+w/jS+GprH3vA978bh3Ejtx2H8h6A/6cDg04fdFLrJ5UOOd3F+KsLB6uD8JHfTXkVBoKowD3nM+PH4Rh8WrQVGiOCzHRZq5tnn3fqkZbstQkfP6u+NgsvgGwCykiM8bwCNV4Raf0i5uXwgRF8KFZwTjcCCMx0MBltudF5WyfHocv+c94zNWlTIUoEmq4HB8XpYT8P6akBMJOkd30vJa81TVOX+gwU75rUKkJ5KFrQidxuPnvcHJyiLCZbGt3OBt79gdj+4rHw8c6v7iAfMFI77z+Mf+iYg/gIPTgXGgRvDRoSG3uq9UYAUZViHeQCA0DQcSRLIH4bZVfk/PeP0RfNo3g8O+iRCEbYTu8zk2P7yr1QjZzLysiJlrahu7g8VEOR2Hm1lCXKTsHqbxSQoCRLOc8UU0Ph2fh3LSOOPapvFCPE5TGdVyxHVEbSwQTirFZSJKc2rznCqmejGhswkhQ3txTCnLJARpLivMUfUAlZzT4V4qjV4Zc/cN98Yk5/ikgQ8BbiAn1Hpx1inJEnUmhUx8Xj044+ocjAmzbuL2uAfdJ2Lx4SF3/+Dg7PDwMU//0MDQcbfQqdkUOksVqqjD26+YleG5qORKyHOidComS3Oyn4y9/95lj/ta6H3/kl+tSQuL1EmEjKCZZQlIGnfG551ZQe3unJhX5KSYTXaOLo51etwnOntxZ1DOjHlPjSuCRAx2/7FOtam8yJmUY2KCquZTHrVli5uC7MzKSlKzeSWiyCJRG9jkLIVYnYSmMxpHkynYn23spEyoZo3LSno7Ny1mqFqbFpLUCTsKQT11ZNNUcUKipYx6JSCrYiIhuAb73Lh7SpSyV0dx0ST2uEdxtH+oB3tTqQSdobFzYsY1OHCib+A47j53NhKY6sUJcYHiMzS+IPdgI3rqgrj73OyHA0ZsOCzMCopYXKk2XXUq9EoWYqDEuSRm5rWGC4Gps7Af5wtsdeh7bY4rTSXilDOpU6l5qIMxdgCaukBSETKyMhYz5tSflnTFxAVFvmZoiEkuloJ0cZOFeEaUpTGD6EpnhPjC2BKNCalUl0KJqNB4xplVEmMVy+BLhS1L95gVB/s8agSgTu1gjVWKy3DxkpRNxqhyqeD+IlXEWTEuGFqKAgWHCvG4NSvYv9pj0awS7J5Wa7CDhgrNBo4sinGqtpUsMllmry9GXD0mzTZPBQLOPvkr+PWEfXll4dMNGT0hDO0Bby7fU7tKi4WU2LddwaLHCNWVFuekbApCbIe1mpWFkj1oKnYR1v5yD1/bKF0bjkP7fXRnM/fbjZXfAXx0G3unprbiguuH79n5ctN+ve72dGj2YqGnoVNAY0xfg5pPapwqzIuSxqUUUYJzLEqpbAb2OBlTNIvBycgZIaHZizvo0axQfp4y3W/Q/cputiUl5gB8RMtZWGyZo6CBHQ2PVgvFnMmmL8VZYzB4sDYlp4sCA39A37IP8Kd1/mAwNMGSNx66+NR+EhpJNkHfUTzGpzpC6TYLQrrFZDKto5b8TmMd1eTM12uWD6+ilrXtnLxjeBWNrKGRPBrRzfts1hynn0QmPsfl6Ad11+tydTsIrnOO3HS+1rPK9a9x/TnrOl+Tiy8fWj6Ub+pfdQysOQZW+WNr/LEct444UIhMNts3yGSyf8eAbgBri8O8zjXlmw/rFkAfc/XLVOcA03nENyzP6TaG2xlO9RqGOxC/K7/riF7LiDqDOKnXM6IB8e359lG9kRFNiG/MN76rNzOiBfHNN9v0Voa3AZ5vHtXbGdGB+N13rfouhu9G/J67PfobDN+D+I6bc/pehr/J8Fl9H8PfYnhSf5vhGPEtOkKtp836fkZ3gq787m79ABA5u96F+B+ZvrKucpN538wqN5OzPm7N6ma0612zzllAHlkMOYgtYspHLqxyF0DE0bDe3L5e36rbrDyIAMhZIcr6A7CyaaJypc0OueVrl30/W8gtrNvblu2/qLsZ+bw7bz+6aj+6Zj+aOwSbtMZ13LX8jdub5/auW2uWPR+czfkAyfmWp/OO/YWxau1cs3bmjfHYan+1utpBV32+452vruanL+bt0VV7dM0e/Z/0QVlwNfphZKsrBK13G1UKmbJZv0FWE/cdA/qzQHHB6fgPYC3w5g=='))))