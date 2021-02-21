import boto3
import json
from flask import Flask, request, render_template

app = Flask(__name__,template_folder='templates')

@app.route('/', methods =["GET", "POST"])
def hello():
    if request.method == "POST":
        with open("D:/UI/Hariharan/v1.json") as f:
            data = json.load(f)
        data['Parameters']['KeyName']['Default'] = request.form.get("keyname")
        data['Parameters']['DBUser']['Default'] = request.form.get("dbuse")
        data['Parameters']['DBPassword']['Default'] = request.form.get("dbpass")
        data['Parameters']['DBRootPassword']['Default'] = request.form.get("dbrpass")
        data['Parameters']['InstanceType']['Default'] = request.form.get("itype")
        # print(data['Parameters']['KeyName']['Default'])
        client = boto3.client('cloudformation',
            region_name = 'ap-south-1',
            aws_access_key_id='AKIA4U23ENDO5GNIK4JM',
            aws_secret_access_key='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')
        
        response = client.create_stack(
            StackName="test",
            TemplateBody=json.dumps(data),
            DisableRollback=False,
        )
    return render_template("index.html")


if __name__ == '__main__':
    app.run()



