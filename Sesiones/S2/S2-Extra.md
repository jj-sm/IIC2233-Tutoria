# Lista ligada en Python

---
## Introducción

Una **lista ligada** (singly linked list) es una estructura de datos formada por nodos donde cada nodo contiene un valor y una referencia al siguiente nodo. Es útil cuando necesitas inserciones/eliminaciones eficientes en posiciones arbitrarias (sin indexado aleatorio eficiente).

---
## Paso 1 — Definir el nodo

Cada nodo guarda un valor y un puntero (referencia) al siguiente nodo.

---

```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"Node({self.value!r})"
```

---
## Paso 2 — Definir la clase LinkedList

---

Implementaremos una clase sencilla con métodos comunes: `append`, `prepend`, `find`, `delete`, `insert_after`, y utilidades como `__iter__`, `__len__` y `to_list`.

---

```python
class LinkedList:
    def __init__(self, iterable=None):
        self.head = None
        self._length = 0
        if iterable:
            for item in iterable:
                self.append(item)

    def __len__(self):
        return self._length

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __repr__(self):
        return f"LinkedList([{', '.join(repr(x) for x in self)}])"

    def append(self, value):
        """Añade al final."""
        new = Node(value)
        if not self.head:
            self.head = new
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new
        self._length += 1

    def prepend(self, value):
        """Añade al inicio."""
        new = Node(value, self.head)
        self.head = new
        self._length += 1

    def find(self, value):
        """Devuelve el nodo que contiene value, o None."""
        cur = self.head
        while cur:
            if cur.value == value:
                return cur
            cur = cur.next
        return None

    def delete(self, value):
        """Elimina la primera ocurrencia de value. Devuelve True si se eliminó."""
        cur = self.head
        prev = None
        while cur:
            if cur.value == value:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                self._length -= 1
                return True
            prev = cur
            cur = cur.next
        return False

    def insert_after(self, target_value, value):
        """Inserta `value` después del primer nodo con `target_value`."""
        node = self.find(target_value)
        if not node:
            raise ValueError("Target value not found")
        new = Node(value, node.next)
        node.next = new
        self._length += 1

    def to_list(self):
        return [x for x in self]
```

---
## Ejemplo de uso

```python
ll = LinkedList([1, 2, 3])
print(ll)            # LinkedList([1, 2, 3])
ll.append(4)         # 1 -> 2 -> 3 -> 4
ll.prepend(0)        # 0 -> 1 -> 2 -> 3 -> 4
ll.insert_after(2, 2.5)
ll.delete(3)
print(ll.to_list())  # [0, 1, 2, 2.5, 4]
```

---
## Complejidades (aproximadas)

- `append` (sin tail pointer): O(n)
    
- `prepend`: O(1)
    
- `find` / `delete` (buscar por valor): O(n)
    

---
## Ejercicio corto

Implementa el método `reverse(self)` que **invierte la lista enlazada en su lugar** (sin crear nodos nuevos). Después prueba con `LinkedList([1,2,3])` y verifica que quede `LinkedList([3,2,1])`.

**Pista:** usa tres punteros: `prev`, `current`, `next_node` y recorre la lista cambiando las referencias `next`.

---

Si quieres, puedo añadir la solución del ejercicio o extender la guía (por ejemplo: añadir `tail` para `append` en O(1) o implementar `__getitem__`).