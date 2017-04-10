import tweepy

consumer_key = "xypzp5decloCrjLBA7IXmEixn";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "kLCdCicB8L1zlbFHjqwavWfPRBYfZKTp41LUO6bbA68D0OSXhX";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "843930900937113600-JPgxpgevXW6pVNGEnYLvZ98IETNQsMX";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "X8C4WwEy1TP29mBcQ1dXUoRPXOeYBaCLMTzAnmleJcy1W";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
