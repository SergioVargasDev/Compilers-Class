## 1. Stack (Pila - LIFO)

### Métodos implementados:

- `push(val)`: Agrega un elemento al tope de la pila. Utiliza el método append(), que en Python tiene una complejidad O(1) amortizado, ya que insertar al final de una lista no implica mover los demás elementos. Internamente, Python reserva bloques de memoria más grandes de lo necesario; así, cuando se insertan nuevos valores, normalmente ya existe espacio disponible. Solo cuando se llena la capacidad, la lista se redimensiona y copia elementos, lo cual es más costoso, pero poco frecuente.
- `pop()`: Devuelve y elimina el último elemento agregado. Si la pila está vacía, regresa un mensaje. Esta operación es O(1) porque Python mantiene una variable interna size que guarda la longitud actual de la lista. El pop() simplemente accede al índice size - 1, elimina la referencia poniéndola en NULL y reduce size en 1.
- `peek()`: Muestra el elemento en el tope de la pila sin eliminarlo. Utiliza la misma lógica de indexación que pop, pero omite la parte de eliminar el elemento. Acceder a un índice es O(1) porque se calcula directamente con aritmética de punteros.
- `empty()`: Devuelve True si la pila está vacía, de lo contrario False. Básicamente revisa si la variable interna size es 0. En Python se implementa con la función len(), que no recorre la lista, sino que devuelve directamente el valor de size.
- `size()`: Devuelve el número de elementos en la pila. De nuevo, se usa la función len(), que en Python devuelve en O(1) la longitud almacenada en la variable interna size.

### Pruebas realizadas:

- Se inicializó la pila: [].
  Se agregaron los números:
  push(1) → [1]
  push(2) → [1, 2]
  push(3) → [1, 2, 3]
  push(4) → [1, 2, 3, 4]

- Se eliminaron dos elementos:
  pop() → [1, 2, 3]
  pop() → [1, 2]

- Se verificó si la pila está vacía: False.

- Se consultó el elemento del tope: 2.

---

## 2. Queue (Cola - FIFO)

Para la implementación se utilizó `collections.deque`, que está optimizada para inserciones y eliminaciones en ambos extremos con complejidad constante.

### Métodos implementados:

- `enqueue(val)`: Agrega un elemento al final de la cola. Utiliza el método `append()`, el cual en un deque es O(1) garantizado, ya que la estructura está optimizada para operaciones en ambos extremos.
- `dequeue()`: Elimina el primer elemento de la cola. Se implementa con popleft(), que también es O(1) porque en lugar de desplazar todos los elementos como haría list.pop(0), simplemente mueve el puntero de inicio al siguiente elemento.
- `front()`: Devuelve el primer elemento sin eliminarlo. Esta operación es O(1) porque el deque mantiene un puntero al inicio, lo que permite acceder directamente al primer elemento.
- `empty()`: Devuelve True si la cola está vacía, de lo contrario False. Internamente revisa la variable size. En Python esto se implementa con la función len(), que devuelve en O(1) la longitud sin recorrer la estructura.
- `size()`: Devuelve el número de elementos en la cola. También utiliza len(), que retorna en \*(1) el valor de la variable interna size.

### Pruebas realizadas:

- Se inicializó la cola: [].

-Se agregaron los números:
enqueue(1) → [1]
enqueue(2) → [1, 2]
enqueue(3) → [1, 2, 3]
enqueue(4) → [1, 2, 3, 4]

- Se eliminaron dos elementos:
  dequeue() → [2, 3, 4]
  dequeue() → [3, 4]

- Se verificó si la cola está vacía: False.

- Se consultó el elemento del frente: 3.

- Se imprimió el tamaño actual: 2.

---

## 3. HashMap

Un HashMap almacena información en forma de pares clave → valor. En Python, esta estructura está implementada como un diccionario (dict), que internamente usa tablas hash.

### Operaciones implementados:

`Insertar valores (hashMap[key] = value)`: Al asignar una clave con un valor, Python calcula un hash de la clave ("name") y lo usa para determinar en qué posición de la tabla hash se guardará el par. Esto toma O(1) en promedio, aunque en casos de colisiones puede degradarse a O(n).

`Acceder a valores (hashMap[key])`: Cuando consultamos algo, Python recalcula el hash de la clave y va directo a la posición correspondiente para devolver el valor. No necesita recorrer todo el diccionario → acceso O(1) promedio.

`Actualizar valores (hashMap[key] = new_value)`: Si la clave ya existe, simplemente se reemplaza el valor asociado en la misma posición de la tabla hash. Esto también es O(1) promedio, porque no cambia la estructura, solo el valor.

`Eliminar claves (del hashMap[key])`: Python calcula el hash de la clave, va a su posición y elimina la entrada. También es O(1) promedio.

`Verificar claves (key in hashMap)`: Python calcula el hash de la clave buscada y revisa si existe en la tabla.Esta operación es O(1) promedio.

`Tamaño del HashMap (len(hashMap))`: Python mantiene una variable interna size que almacena el número actual de pares clave-valor. Consultar el tamaño es O(1) porque solo devuelve ese número.

### Pruebas realizadas:

- Se inicializó el diccionario: {}.

- Se insertaron las claves y valores:
  "name": "Sergio" → {"name": "Sergio"}
  "age": 21 → {"name": "Sergio", "age": 21}
  "city": "Monterrey" → {"name": "Sergio", "age": 21, "city": "Monterrey"}

- Se accedió a los valores:
  "name" → "Sergio"
  "age" → 21
  "city" → "Monterrey"

- Se actualizó "age" de 21 a 22 → {"name": "Sergio", "age": 22, "city": "Monterrey"}

- Se eliminó la clave "city" → {"name": "Sergio", "age": 22}

- Se verificó la existencia de claves:
  "name" in hashMap → True
  "city" in hashMap → False

- Se imprimió el tamaño actual: 2.

---
