def Email_1():
    settings = {}
    from airflow.operators.email import EmailOperator
    from datetime import timedelta

    return EmailOperator(
        task_id = "Email_1",
        to = "sony@prophecy.io",
        subject = "test subject for airflow email from sanity job",
        html_content = "python job - test content for airflow email from sanity job",
        cc = "abhisheks@prophecy.io",
        bcc = None,
        mime_subtype = "mixed",
        mime_charset = "utf-8",
        conn_id = "email_default",
        **settings
    )
