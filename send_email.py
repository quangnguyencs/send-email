if __name__ == "__main__":
    import argparse
    from utils import *

    parser = argparse.ArgumentParser()

    parser.add_argument("--email", type=str, required=True)
    parser.add_argument("--template", type=str, required=True)
    parser.add_argument("--customer", type=str, required=True)
    parser.add_argument("--output", type=str, required=True)
    parser.add_argument("--errors", type=str, required=True)

    args = parser.parse_args()

    assert check_email_format(args.email), "Wrong login email format"

    print("Email: " + str(args.email))
    password = getpass()

    user = yagmail.SMTP(user=args.email, password=password)

    user.login()

    with open(args.template) as template:
        email_template = json.load(template)

    customers_detail = pd.read_csv(args.customer)
    assert len(customers_detail) != 0, "No customer in the file"

    customer_header = customers_detail.columns.to_list()

    errors, success = [], []
    for customer in customers_detail.iloc:
        receiver = apply_detail_to_template(email_template, customer)
        try:
            user.send(
                to=receiver["to"],
                subject=receiver["subject"],
                contents=receiver["body"],
            )
        except:
            print("An except occurs")
            print("Add error into {}".format(args.errors))
            errors.append(customer.to_list())

        else:
            print("Email sent to {}".format(receiver["to"]))
            success.append(receiver)

    add_errors(errors, path=args.errors, csv_header=customer_header)
    add_success(success, path=args.output)

    print("Sent {0}/{1} emails".format(len(success), len(customers_detail)))
    print("Fail to send {} emails".format(len(errors)))
