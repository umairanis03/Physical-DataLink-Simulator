/*Author
Umair Anis B17CS035
Kamal Sharma B17CS028
*/

1. Multiple clients connected with single architecture.
2. All clients can connect simultaneously with threading in server.
3. Limit on number of connections is implemented.
4. Physical Layer & Data-Link Layer is implemented separately , Sender & Receiver inheriting their properties.
5. Physical Layer has Error Maker( produces error), Line Encoding (Bi-Polar NRZ)
6. Data-Link Layer is used to form frames ( variable size frames with bit-stuffing)
7. Error- detection is done through CRC ( at Data-Link Layer)
8. First the string is converted to it's ASCII code, appended then encoding is applied . At receiver's decoding happens in opposite sequence.




Running File (Requires Python 3.x)

1. Run Server.py
2. Run client.py
3. Send message through client.
4. User will be prompted to add error, if added it will be detected at data-link layer at receiver's end.
