# Standard ML

## datatypes

---

### concrete datatypes

* `datatype` creates new types
* datatypes can be constructed and taken apart
* ML's datatypes have two kinds of values: **atomic** and **composite**

---

### enumeration types

```sml
datatype single = only;

only;
```
<!-- .element: data-thebe-executable-sml -->

`only` denotes the only value of type `single` (isomorphic to `unit`)

<!--vert-->

order doesn't matter

```sml
datatype bool = true | false;
```
<!-- .element: data-thebe-executable-sml -->

<!--vert-->

allows pattern matching

```sml
datatype piece = king | queen | rook | bishop | knight | pawn;

fun value king = Real.posInf (*infinity*)
  | value queen = 9.0
  | value rook = 5.0
  | value (bishop | knight) = 3.0
  | value pawn = 1.0;

value bishop;
```
<!-- .element: data-thebe-executable-sml -->

---

### branding

Newton's second law

```sml
fun a m f = f/m;

val (body, engine) = (0.0122, 50.0);

a engine body; (* oops *)
```
<!-- .element: data-thebe-executable-sml -->

<!--vert-->

type aliasing doesn't help

```sml
type mass = real and force = real and acceleration = real;

fun a (m:mass) (f:force) : acceleration = f/m;

a engine body; (* still oops *)
```
<!-- .element: data-thebe-executable-sml -->

<!--vert-->

simulate branding using `datatype`

```sml
datatype mass = Kg of real;
datatype force = Newton of real;
datatype acceleration = m_s'2 of real;

fun a (Kg m) (Newton f) = m_s'2 (f / m);

val body = Kg 2.0;
val engine = Newton 50.0;

a body engine; (*OK*)

a engine body; (*Error*)
```
<!-- .element: data-thebe-executable-sml -->

---

### constructors

constructors are functions

```sml
datatype mass = Kg of real;
datatype force = Newton of real;
datatype acceleration = m_s'2 of real;

Kg;

Newton;
```
<!-- .element: data-thebe-executable-sml -->

---

### variant types

```sml
datatype shape =
    point
  | Line of real
  | Circle of real
  | Rectangle of real*real;

fun area (point | Line _) = 0.0
  | area (Circle r) = Math.pi*r*r
  | area (Rectangle (w, h)) = w * h;
```
<!-- .element: data-thebe-executable-sml -->

---

### pattern matching

```sml
val line = Line 5.3;
```
<!-- .element: data-thebe-executable-sml -->

```sml
val Line length = line;
```
<!-- .element: data-thebe-executable-sml -->

```sml
val Circle radius = line;
```
<!-- .element: data-thebe-executable-sml -->

<!--vert-->

⚠️ constructors cannot be rebound by `val`

```sml
val point = point; (*OK*)
val point = 5.3; (*Error*)
```
<!-- .element: data-thebe-executable-sml -->

---

### recursive datatypes

🛈 every list is either `nil` or `head::tail`

```sml
datatype intlist =
    nil
  | :: of int * intlist;

fun length nil     = 0
  | length (x::xs) = 1 + length xs;
```
<!-- .element: data-thebe-executable-sml -->

---

### polymorphic datatypes

```sml
datatype 'a list =
    nil
  | :: of 'a * ('a list);
```

```sml
"hello" :: "world" :: nil;
```
<!-- .element: data-thebe-executable-sml -->

<!--vert-->

```sml
datatype 'a option = NONE | SOME of 'a;

fun head []     = NONE
  | head (x::_) = SOME x;

head [1, 2, 3];

head (tl [1]);
```
<!-- .element: data-thebe-executable-sml -->

<!--vert-->

```sml
datatype ('a, 'b) union = type1 of 'a
  | type2 of 'b;

val five = type1 5;

val hello = type2 "hello";

val five_or_hello = if true then five else hello;

val int_char_list = [type1 5, type2 #"a"];
```
<!-- .element: data-thebe-executable-sml -->

---

### trees

```sml
datatype 'a tree =
    Nil
  | Br of 'a * ('a tree) * ('a tree);

fun Leaf x = Br (x, Nil, Nil);

val tree2 = Br (2, Leaf 1, Leaf 3);
val tree5 = Br (5, Leaf 6, Leaf 7);
val tree4 = Br (4, tree2, tree5);
```
<!-- .element: data-thebe-executable-sml -->

```sml
fun size Nil = 0
  | size (Br (v,t1,t2)) = 1 + size t1 + size t2;

size tree4;
```
<!-- .element: data-thebe-executable-sml -->

---

### binary search trees

* implement an associative array using trees
* the keys are `int`s
* values may be anything
* assumption: the tree is sorted

<!--vert-->

```sml
val cmp = Int.compare;

fun get (Br ((node_k, v), left, right)) k = 
  case cmp (node_k, k) of
    EQUAL   => v
  | GREATER => get right k
  | LESS    => get left k
;
```
<!-- .element: data-thebe-executable-sml -->

<!--vert-->

```sml
local
   fun compare (k1,_) (k2,_) = cmp (k1, k2)
in
    fun insert Nil item = Br (item, Nil, Nil)
      | insert (Br (node, left, right)) item = 
        case compare node item of 
          EQUAL   => Br (item, left, right)
        | GREATER => Br (node, left, insert right item)
        | LESS    => Br (node, insert left item, right)
end;
```
<!-- .element: data-thebe-executable-sml -->
