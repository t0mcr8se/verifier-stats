# API DOC

for swagger: /schema/swagger-ui

## List node
`GET /nodes`

## Retrieve node by id
`GET /nodes/{id}`

## Create new node
`POST /nodes`

body example:
```
{
    "ip_address": "192.168.1.9",
    "name": "node_name",
    "type": "node_type",
    "last_block": 1337,
    "pending_transactions": 31337
}
```

## Update all nodes
`POST /nodes`

body example:
```
[
    {
        "ip_address": "192.168.1.7",
        "name": "node1",
        "type": "node_type",
        "last_block": 1337,
        "pending_transactions": 31337
    },
    {
        "ip_address": "192.168.1.9",
        "name": "node2",
        "type": "node_type",
        "last_block": 1337,
        "pending_transactions": 31337
    }
]
```

## Delete node by id
`DELETE /nodes/{id}`