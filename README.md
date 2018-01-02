# msh-domain-enterprise
Domain enterprise

Link to main project: [Domain Objects](https://github.com/fbrump/msh/blob/master/README.md#enterprise)

Propose models:

- Employer
  * id
  * code
  * name
  * birth date
  * Position (ref.)
  * Company (ref.)
  * Contact Mail (ref.)
  * List Contact Phone (ref.)
  
- Manager
  * id
  * code
  * name
  * Position (ref.)
  * Company (ref.)
  * Contact Mail (ref.)
  * List Contact Phone (ref.)

- Contact Phone (~Employer~ Contact Phone)
  * id
  * country code (+55 Brazil)
  * city code (21, 11)
  * line
  
- Contact Mail (~Employer~ Contact Mail, ~Manager~ Contact Mail)
  * id
  * tyeMail
  * address
  
- Position
  * id
  * code
  * name
  * job description

- Company
  * id
  * code
  * name
  * cnpj
  * description
