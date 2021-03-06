# Design

### Key Concepts

* A signature together with a squeak's public key (ECDSA) proves authorship of the squeak.
* A decryption key (RSA) together with a squeak proves ownership of the squeak's unencrypted content.
* A squeak's block hash (SHA-256) proves minimum creation time of the squeak.
* A squeak's hash (SHA-256) is unique and derived from all fields in the squeak's header.

### Design Decisions

* Use the same cryptography primitives as Bitcoin wherever possible.
* Squeak content is 1120 bytes. This is enough for 280 UTF-8 characters.
* Hybrid RSA/AES encryption is used to keep the size of squeak header small.
* Buyer only sends Payment after seller proves validity of a squeak and ownership of its private key.
