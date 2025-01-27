## Send Email Integration

Resend.com Email Integration With Frappe Framework

#### License

mit

## steps for installation of app

1 - bench get-app https://github.com/ahmedatef9693/Sending-Email-Integration.git
2 - bench --site <site-name> install-app send_email_integration

## steps for using the app

1 - head over to resend site and generate new api key https://resend.com/api-keys
add the following api key in (Resend Integration Settings) Screen

2 - head over and set the hooks callback function https://resend.com/webhooks ===> https://<your-site-domain>/api/method/send_email_integration.api.handle_resend_webhook

3 - also add your signning secret for security in (Resend Integration Settings) Screen
