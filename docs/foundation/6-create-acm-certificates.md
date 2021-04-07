---
layout: default
title: 6. Configure ACM Certificates
parent: Foundation
nav_order: 6
has_children: true
---

## DNX Tutorial - How to create ACM certificates

| Version  | 1.0             |
| -------- | --------------- |
| Author   | Marcus Nogueira |
| Revision | Pietro Marmelo  |


To enhance the security of the environment, Well Architected Foundation needs valid certificates. AWS offers this service free of charge for services that are within its infrastructure.

The Well Architected Foundation needs to create certificates in two regions:

us-east-1 (North Virginia) and the region where the resources were created (workload region). Example ap-southeast-2 (Sydney).

The Northern Virginia region is needed, because global resources like CloudFront are managed in that region.

This document is intended to demonstrate the steps to create the certificates needed to use on Well Architected Foundation.

### Topics:

 - Request ACM certificates

### Request a certificate.

 Log into AWS Console.
1. Switch to specific account (e.g.: nonprod or prod).

2. Choose the first region (us-east-1 or workload region).

3. Go to Services → ACMc(Certificate Manager).
   ![ACM_001](/assets/images/ACM_01.png)

4. Choose Request a certificate.
   ![ACM_002](/assets/images/ACM_02.png)

5. On the Request a certificate page, choose Request a public certificate and Request a certificate to continue.
   ![ACM_003](/assets/images/ACM_03.png)

6. On the **Add domain names page**, type your domain name.
   *You can use a fully qualified domain name (FQDN), such as www.example.com, or a bare or apex domain name such as example.com. You can also use an asterisk (*) as a wild card in the leftmost position to protect several site names in the same domain. For example, *.example.com protects corp.example.com, and images.example.com. The wild card name will appear in the Subject field and the Subject Alternative Name extension of the ACM certificate.*

   ![ACM_004](/assets/images/ACM_04.png)
   To add another name, choose Add another name to this certificate and type the name in the text box. This is useful for protecting both a bare or apex domain (such as example.com) and its subdomains such as *.example.com).
   
7. When you finish adding names, choose **Next**.

8. On the **Select validation method page**, choose either DNS validation or Email validation, depending on your needs. If you are able to edit your DNS configuration, we recommend that you use DNS domain validation rather than email validation.
   Before ACM issues a certificate, it validates that you own or control the domain names in your certificate request. You can use either email validation or DNS validation. If you choose email validation, ACM sends validation email to three contact addresses registered in the WHOIS database and to five common system administration addresses for each domain name. You or an authorized representative must reply to one of these email messages. For more information, see [Using Email to Validate Domain Ownership](https://docs.aws.amazon.com/acm/latest/userguide/email-validation.html). If you use DNS validation, you need to add a CNAME record provided by ACM to your DNS configuration. For more information about DNS validation, see [ Using DNS to Validate Domain Ownership](https://docs.aws.amazon.com/acm/latest/userguide/dns-validation.html).

9. On the **Add tags page**, you can optionally tag your certificate. Tags are key/value pairs that serve as metadata for identifying     and organizing AWS resources. For a list of ACM tag parameters and for instructions on how to add tags to certificates after creation, see [Tagging AWS Certificate Manager Certificates](https://docs.aws.amazon.com/acm/latest/userguide/tags.html).

10. When you finish adding tags, choose **Review**.

11. If the Review page contains correct information about your request, choose **Confirm and request**. A confirmation page shows that your request is being processed and that certificate domains are being validated. Certificates awaiting validation are in the Pending validation state. After choosing a validation method, choose **Next**.

12. **You need to repeat the entire process in the next region**.

    

