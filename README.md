# personaldatabroker

Personal Data Broker (PDB) enables 21 network members to sell their personal data to third parties.  The personal data is always under the user's control and is only sold at terms and prices agreed to by the user.  At the user's discretion, the user may opt into the PDB aggregator, which distributes queries to all member nodes.

## Installation

## Setup

PDB accepts data purchase requests in the format /buy/dataset. Each data set corresponds to a set of values that describe an individual's attributes and preferences.  By default data sets are provided as JSON.  In version 1.0 data sets are stored as static files.   PDB ships with the following JSON templates:

* **basics **(demographics)
* **interests **(keywords and unstructured text)
* **IAB** (Internet Advertising Bureau shopping categories)
* **BISAC** (book catalog categories)
* **Myers-Briggs** scale
* **OCEAN** scale

Users may offer some, all, or none of these data sets via PDB.

Joining the aggregator increases the number of opportunities to sell personal data since the aggregator can send queries to all member nodes.  Joining the aggregator is optional.  To join, go to PageKicker.com/pdb and submit your 21 network ipV6 address.
