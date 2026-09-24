---
tags: [aws, dop-c02, domain-2, cloudfront, encryption]
read: false
---

# CloudFront Field-Level Encryption

CloudFront field-level encryption encrypts selected sensitive request fields at the edge with a public key. The encrypted values remain protected through intermediaries and can be decrypted only by a component holding the private key.

```text
viewer HTTPS request
  → CloudFront encrypts selected POST fields
  → origin/application sees ciphertext
  → authorized component decrypts
```

Use when only a specific downstream component should read data such as a payment field.

Do not confuse:

- HTTPS: encrypts transport links.
- Signed URL/cookie: controls access to private content.
- Origin Access Control: restricts access to an S3 origin.
- Field-level encryption: protects selected application fields end to end through the stack.

Source: [CloudFront field-level encryption](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.html)

## Setup and limitations

Use a 2048-bit RSA key pair, upload the public key, create a profile defining selected POST fields, create the configuration, and attach it to a cache behavior. Protect the private key in the authorized decrypting component.

CloudFront encrypts up to 10 selected fields, not the entire body. The origin must support chunked encoding. This is additional application-field protection, not a replacement for HTTPS or access authorization.
