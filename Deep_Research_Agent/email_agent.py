from agents import Agent,function_tool
import os
from typing import Dict
from sendgrid.helpers.mail import Mail,To,Email,Content
import sendgrid

@function_tool
def send_email(subject: str, html_body: str) -> Dict[str,str]:
    """ Send out an email with the given subject and HTML body """
    sg = sendgrid.SendGridAPIClient(api_key=os.getenv('SENDGRID_API_KEY'))
    from_email = Email('tycoon1156@gmail.com')
    to_email = To('anandreddy.s3215@gmail.com')
    content = Content("text/html",html_body)
    mail = Mail(from_email,to_email,subject,content).get()
    response = sg.client.mail.send.post(request_body=mail)
    return {"status":"success"}

INSTRUCTIONS = """ You are able to send a nicely formatted HTML email based on a detailed report.
You will be provided with a detailed report. You should use your tool to send one email, providing the report converted into
clean, well presented HTML with an appropriate subject line.
"""

email_agent = Agent(
    name="Email Agent",
    instructions=INSTRUCTIONS,
    tools=[send_email],
    model="gpt-4o-mini"
)