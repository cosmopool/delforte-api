# Clients
---
## Client
Manage client main information.

### Get client info
__GET__ | `/clients/{client_id}/`

### Add client
__POST__ | `/clients/`

### Edit client
__PATCH__ | `/clients/{client_id}/`

### Remove client
__DELETE__ | `/clients/{client_id}/`

---
## Address
Manage specific client addresses.

### Add address
__POST__ | `/clients/{client_id}/address`
Add address to a specific client.

### Remove address
__DELETE__ | `/clients/{client_id}/address`
Remove address from a specific client.

### Edit address
__PATCH__ | `/clients/{client_id}/address`
Edit address from a specific client.

---
`TODO: Phones will not be implemented in api V1`
## Phones
Manage specific client phone numbers.

### List all phone numbers
__GET__ | `/clients/{client_id}/phone/`
List all phone numbers from a specific client.

### Add phone number
__POST__ | `/clients/{client_id}/phone/`
Add a phone number to a specific client.

### Edit phone number
__PATCH__ | `/clients/{client_id}/phone/{phone_id}`
Edit a phone number from a specific client.

### Remove phone number
__DELETE__ | `/clients/{client_id}/phone/{phone_id}`
Delete a specific phone number from a specific client.

---
`TODO: History will not be implemented in api V1`
## History
Get information specific client appointments/tickets history.
### Get info on appointments history
### Get info on tickets history

---
# Tickets

### Open ticket
__POST__ |`/tickets/`
Open a new ticket

### Get ticket info
__GET__ |`/tickets/{ticket_id}/`
Get information about a specific ticket

### Close ticket
__POST__ |`/tickets/{ticket_id}/actions/close/`
Close a open ticket

### Edit ticket
__PATCH__ |`/tickets/{ticket_id}/`
Edit a specific ticket

### Delete ticket
__DELETE__ |`/tickets/{ticket_id}/`
Delete a specific ticket

---
# Appointments

### Book appointment
__POST__ |`/tickets/`
Book a new appointment.

### Get appointment info
__GET__ |`/appointments/{appointment_id}/`
Get info on a specific appointment.

### Close appointment
__POST__ |`/appointments/{appointment_id}/actions/close/`
Close a specific appointment.

### Edit appointment
__PATCH__ |`/appointments/{appointment_id}/`
Edit a specific appointment.

### Delete appointment
__DELETE__ |`/appointments/{appointment_id}/`
Delete a specific appointment.

### Reschedule appointment
__POST__ |`/appointments/{appointment_id}/actions/reschedule/`
Reschedule a specific appointment to a new date.

