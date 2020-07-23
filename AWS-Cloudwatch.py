__Author__ = 'Prameet Bisht'
__Version__ = "0.0.1"
__Email__ = "myprameet09@gmail.com"
__Github__ = "https://github.com/orgs/POC-AWS-services/dashboard"


try:
    import boto3
    import os
    import sys
    import pandas as pd
    import csv
    print("All Modules are Loaded ......")
except Exception as e:
    print("Some Modules are missings {}".format(e))


class CloudWatch(object):
    def __init__(self):
        self.client = boto3.client('logs')
        self.timestamp = []
        self.message=[]

    def get_logs(self, logGroupName='your_group_name',logStreamName='your_log_stream' ):
        """
        :param logGroupName: Takes String
        :param logStreamName: Takes String
        :return: Pandas Dataframe
        """
        response = self.client.get_log_events(
            logGroupName=logGroupName,
            logStreamName=logStreamName)
        for x in response.get("events"):
            self.timestamp.append(x.get("timestamp", None))
            self.message.append(x.get("message", None))

        df = pd.DataFrame({
            "TimeStamp":self.timestamp,
            "Message":self.message
        })
        return df

    def save_csv(self):
        df = self.get_logs()
        df.to_csv("Report.csv")
        print("Saved CSV FIle on your Computer ")

    def save_json(self):
        df = self.get_logs()
        df.to_json("Report.json")
        print("Saved JSON File on your Computer ")

    def save_html(self):
        df = self.get_logs()
        df.to_html("Report.html")
        print("Saved HTML File on your Computer ")


if __name__ == "__main__":
    obj = CloudWatch()
    df1 = obj.get_logs(logGroupName='your_group_name',logStreamName='your_log_stream')
    print(df1)
    print(obj.save_csv())
    obj.save_json()
    obj.save_html()