from flask import (
    Flask, 
    render_template, 
    url_for, 
    request, 
    redirect
    )
import os
import csv

current_dir = os.getcwd()
print(current_dir)

app = Flask(__name__)
if __name__ == "__main__":
    print(__name__)

@app.route('/')
def landing():
    return render_template("index.html")


@app.route("/<string:my_page>")
def webpage(my_page):
    return render_template(my_page)


def writer(submission_data):
    with open(f"{current_dir}/database.txt", mode="a") as database:
        email = submission_data['email'] 
        subject = submission_data['subject'] 
        message = submission_data['message'] 
        my_file = database.write(f"\n{email}, {subject}, {message}")


def csv_writer(submitted_data):
    with open(f"{current_dir}/database.csv", newline='', mode="a") as database_csv:
        email = submitted_data['email'] 
        subject = submitted_data['subject'] 
        message = submitted_data['message'] 
        '''csv_writer is an object that you can use.'''
        csv_writer = csv.writer(database_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route("/submit_form", methods=["POST", "GET"])
def contact_me():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            data2 = request.form["message"] 
            writer(data)
            csv_writer(data)
            print(data)
            return redirect("/thankyou.html")
        except:
            return f"The Following Data Could Not Be Written To DB\n{data}"
    else:
        return "Something Went Wrong (Possibly Horribly)"
