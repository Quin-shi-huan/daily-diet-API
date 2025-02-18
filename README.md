
# Diet API

This is a CRUD API for meal management, aiming to record your meals and keep you on your diet if you are.


## Routes 🏁

#### Returns all registered meals

```
  GET /diet
```

| Route   |Description| 
| :---------- | :---------------------------------- |
| `/diet`| Return route for all registered meals |


#### Create meals

```
  POST /diet
```

| Route  |Descrição|
| :---------- | :---------------------------------- |
| `/diet`| meal creation route |


#### Updates an already created meal
```
  PUT /diet/id
```

| Route   | `id` | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `/diet` | `Number` | Update route for an already created meal |

#### Returns a specific meal already registered
```
  GET /diet/id
```

| Route   | `id` | Description                          |
| :---------- | :--------- | :---------------------------------- |
| `/diet` | `Number` | Reading route for a specific meal |


#### ⚠ Resets AUTO_INCREMENT ( ` Commented ` ) ⚠


```
  GET /reset_ids
```

| Route   | Description
| :---------- |:---------------------------------- 
| `/diet` | Resets AUTO_INCREMENT so that at each startup the first meal created is `id = 1` |

