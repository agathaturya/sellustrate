#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 14:47:29 2018

@author: vivekmishra
"""


#API for checking fulfillment
import requests

token = "v^1.1#i^1#r^0#p^3#f^0#I^3#t^H4sIAAAAAAAAAOVYa2wURRzv0QfylA8IAo0eK0J47N3s414benh9YCv0AVcqYLCd3Z1t1+7tXnZmez0VaWqsmpB+MIqJCdCECiFRggbQmmgIicGkRj5pNKJNUHlJaKIiBo04e31da4Q++NDEyyWbmfm/fr///z87s6CtYNaajvKOm/M8M2d0tYG2GR4PNwfMKshfOz93xtL8HJAl4OlqW9GW1557eT2GCSMpbUU4aZkYeVsThomlzGQR49imZEGsY8mECYQlokjxWOVmifcBKWlbxFIsg/FWlBYxwYgialBFwQCnBmBQpLPmkM1aq4hRIB/UtJAsh1VRUYIBuo6xgypMTKBJihgecGEWCPRfy/OSGJCEsE/kxZ2Mtw7ZWLdMKuIDTDQTrpTRtbNivXOoEGNkE2qEiVbENsarYxWlZVW16/1ZtqKDPMQJJA4ePSqxVOStg4aD7uwGZ6SluKMoCGPGHx3wMNqoFBsKZhLhZ6gWhCCUtRDPC1xI1eC9oXKjZScguXMc7oyuslpGVEIm0Un6boxSNuRnkEIGR1XUREWp131scaChazqyi5iy4tiObfGyrYw3XlNjWy26ilQXKScIEYHnIyITJQhTCpFd35LQcZMNgTjobMDiINVjvJVYpqq7xGFvlUWKEY0cjeVHyOKHClWb1XZMI25Uw3JiLQBDPHKBnW5iBzLpkCbTzS1KUDK8meHdszBUFiOFcK8KQ+VVQRAjgqiFkApCYFRhuL0+yeKIuvmJ1dT43ViQDNNsAtrNiCQNqCBWofQ6CWTrKuVS44Wwhlg1GNFYMaJprBxQgyynIQQQkmUlEv6/1Qghti47BA3XydiFDNAiJq5YSVRjGbqSZsaKZPaewapoxUVMEyFJye9PpVK+lOCz7EY/DwDn3165Oa40oQRkhmX1uwuzeqY+FES1sC6RdJJG00rLjzo3G5moYKs10CbpYidNx3FkGPQxVMKjIoyOnf0PqNiFOr1AuvqYGoBJ3edWuE+xEn4L0o52p+ozEXvHI+SXnTT1ryLbZyOoWqaRHr9eo0MreEB7fEqYZsM30IwUxrBHt9cnY2ACOrrZQmvZstMThDlaeQI6UFEsxySTcTeoOgENzTE03TDcdp2Mwyz1iYRpQiNNdAVPxmXWjkzpxXpjExmxM6VujSWTFer06tY6vQU1V+qYdaE7dJaNF29neVULhkBYi7BqSFFlMRSYEm4VtegKqtenGXbTMYxsBG6vTxhbKWqZbjlFwZDIRXiBVYKawooyz7MQ0VyKfFDgIVKDXEScUj4rG6dbKqv8sSkhKjF0usPUpqfby7TcwgSpU4NGz7XTC5S7wwxtMIGwKLAiAAFWVDWRlcMRmRVC4XFDHjORdTT8183An309z8vFKJqT+XHtno9Bu6eH3vHpSZ/l1oLVBbnb8nLnMlgnyIehqcpWq0+Hmo++DEx6/7SRrxmlk1C3ZxR4nlp2dcNfWZ8GunaBB4c/DszK5eZkfSkAhSMr+dz9i+dxYSAAeuYWA0J4J3hkZDWPW5S3cG3+rY7zxzr/7Ok5fv3wMqA47Qu+AvOGhTye/Jy8dk/Ouu3nj350aPHC+as/7/bIJzrLt30/++be3jr4dBu38tV+4/X79l3L2/N1SWd/36prC+CVrobWlVVnlm9J/lB9+sDvvzrB6m5f/WelWzuiZ9fVSOF3+0nDY82r3j5kLLqReuJ22czaF75b8fDJ566e7bt8Xbt44sI7524t3n1maYM/3p36UFh+9NQf+QeZHvlAz49vXkqlLuz9gn//g30VjD5b7tvRefWnxt/OLdlxo2/J3CuF5/eTb7+8+doD7/38RuhI+OKnp54/hn/xfHN7EdjVveeV3vIqboP38IsHG166Nv90z8bU31qypPehTza9fPxSXvR6b+5+8Oy5xx+Nv7VpzZrC/LLdT8ZOHunPKewZSOM/yT2habQRAAA=" 


headers = {'Authorization': 'Bearer '+token,
           'Content-Type':'application/json',
           'X-EBAY-C-MARKETPLACE-ID':'EBAY_US'}
body = {
    "availability": {
        "shipToLocationAvailability": {
            "quantity": 50
        }
    },
    "condition": "NEW",
    "product": {
        "title": "GoPro Hero4 Helmet Cam",
        "description": "New GoPro Hero4 Helmet Cam. Unopened box.",
        "aspects": {
            "Brand": [
                "GoPro"
            ],
            "Type": [
                "Helmet/Action"
            ],
            "Storage Type": [
                "Removable"
            ],
            "Recording Definition": [
                "High Definition"
            ],
            "Media Format": [
                "Flash Drive (SSD)"
            ],
            "Optical Zoom": [
                "10x"
            ]
        },
        "brand": "GoPro",
        "mpn": "CHDHX-401",
        "imageUrls": [
            "http://i.ebayimg.com/images/i/182196556219-0-1/s-l1000.jpg",
            "http://i.ebayimg.com/images/i/182196556219-0-1/s-l1001.jpg",
            "http://i.ebayimg.com/images/i/182196556219-0-1/s-l1002.jpg"
        ]
    }
}
url = 'https://api.sandbox.ebay.com/sell/inventory/v1/inventory_item/apple_watch'
r = requests.get(url, headers=headers,data= body)
returns = r.json()


https://hacktech2018@sellustrate.scm.azurewebsites.net/sellustrate.git
hacktech2018
sellustrate
https://sellustrate@sellustrate.scm.azurewebsites.net/sellustrate.git
https://sellustrate@sellustrate.scm.azurewebsites.net/sellustrate.git




