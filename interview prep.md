# Interview Prep: Core Programming and Cloud Concepts

## 1. What is asynchronous programming in JavaScript/Node.js?

Asynchronous programming lets a program start an operation that may take time—such as a network request, file read, or timer—without blocking the thread while it waits. The program can continue doing other work and handle the result when it becomes available.

This matters in JavaScript because JavaScript code generally runs on one main thread. In Node.js, many I/O operations are coordinated by the runtime and operating system (and some work uses the libuv thread pool). When an operation completes, its callback or continuation is scheduled to run. The **event loop** coordinates this work: it runs queued callbacks when the call stack is clear. Promise reactions (including code after `await`) are scheduled as microtasks and are generally processed before the next event-loop task.

### Common approaches

- **Callbacks:** A function is passed to run later. This is simple, but deeply nested callbacks can become difficult to read and error-prone.
- **Promises:** A `Promise` represents an eventual result or failure. `.then()` handles fulfillment and `.catch()` handles rejection.
- **`async` / `await`:** Syntax built on Promises that makes asynchronous control flow read more like sequential code. An `async` function always returns a Promise, and `await` pauses that function until the awaited Promise settles; it does not block the JavaScript thread.

```js
async function loadUser(id) {
  const response = await fetch(`/api/users/${id}`);
  if (!response.ok) {
    throw new Error(`Request failed: ${response.status}`);
  }
  return response.json();
}

loadUser("42")
  .then((user) => console.log(user))
  .catch((error) => console.error("Could not load user:", error));
```

Independent asynchronous operations can often run concurrently:

```js
const [profile, settings] = await Promise.all([
  fetch("/api/profile").then((response) => response.json()),
  fetch("/api/settings").then((response) => response.json()),
]);
```

`Promise.all` rejects if any input Promise rejects. If every outcome should be collected, including failures, consider `Promise.allSettled`.

### Important distinction

Asynchronous does not automatically mean CPU work runs in parallel. A long, CPU-intensive loop on the main JavaScript thread still blocks it. For CPU-heavy work, use mechanisms such as worker threads in Node.js or Web Workers in browsers.

**Interview summary:** “Asynchronous programming allows JavaScript to handle I/O without blocking the main thread. The event loop schedules callbacks and Promise continuations; Promises and `async`/`await` provide structured ways to manage results and errors.”

## 2. What is the Virtual DOM in React?

The **Virtual DOM** is a commonly used name for React's in-memory representation of the UI. In modern React, this is represented by React elements and the Fiber data structure; it is not a second browser DOM. Components produce descriptions of what the UI should look like based on props and state.

When state or props change, React renders an updated description and compares it with the previous one. This comparison and update process is commonly called **reconciliation**. React determines which changes are needed and commits appropriate updates to the actual browser DOM (or to another rendering target, such as native views in React Native).

### Simplified flow

1. A component renders a description of the UI from its current props and state.
2. An update triggers React to render the affected component tree.
3. React reconciles the new description with the previous one, using element types and keys to identify corresponding children.
4. React commits the necessary changes to the host environment, such as the browser DOM.

```jsx
function Counter() {
  const [count, setCount] = React.useState(0);

  return (
    <button onClick={() => setCount((current) => current + 1)}>
      Count: {count}
    </button>
  );
}
```

When the button is clicked, React renders the component with the new `count`. React then updates the relevant UI rather than requiring the developer to manually find and change DOM nodes.

### Why it is useful

- It supports a declarative programming model: describe the UI for a given state, and React manages updates.
- It helps React coordinate and organize UI changes.
- It abstracts many low-level DOM operations from application code.

The Virtual DOM should not be described as *always faster* than direct DOM manipulation. Rendering and reconciliation have costs; React's value is primarily its declarative model and managed update process, with performance depending on the application and implementation.

**Interview summary:** “The Virtual DOM is React's in-memory representation of the UI. On updates, React reconciles the new tree with the previous one and commits the necessary changes to the actual rendering environment.”

## 3. What is exception handling in Python?

**Exception handling** is the process of responding to errors or unusual conditions that occur while a program runs. Python signals many such conditions with exceptions. Handling them lets a program recover, report a useful message, or clean up resources instead of terminating unexpectedly.

### Main constructs

- `try`: Contains code that may raise an exception.
- `except`: Handles a specified exception type.
- `else`: Runs only when the `try` block completes without an exception.
- `finally`: Runs whether or not an exception occurred; useful for cleanup.
- `raise`: Raises an exception explicitly or re-raises the current exception.

```python
def read_integer(text):
    try:
        value = int(text)
    except ValueError as error:
        raise ValueError(f"Expected an integer, got {text!r}") from error
    else:
        return value
    finally:
        print("Conversion attempt finished")
```

Catch the narrowest exception type the code can reasonably handle. Catching a broad `Exception` without a clear recovery plan can hide programming errors. If an error cannot be handled meaningfully at the current level, allow it to propagate or re-raise it after adding useful context.

For resource cleanup, Python's context managers are usually clearer and safer than manually relying on `finally`:

```python
with open("data.txt", encoding="utf-8") as file:
    contents = file.read()
```

The file is closed when execution leaves the `with` block, including when an exception occurs.

Custom exception types can make an application's error cases explicit:

```python
class UserNotFoundError(Exception):
    pass


def get_user(user_id):
    user = lookup_user(user_id)
    if user is None:
        raise UserNotFoundError(f"No user found for id {user_id}")
    return user
```

**Interview summary:** “Python exception handling uses `try` and `except` to handle specific runtime errors. `else` runs when no error occurs, `finally` is for unconditional cleanup, and `raise` signals or propagates an error. Specific exceptions and context managers make handling safer.”

## 4. What is a REST API, and how does it work?

An **API** (Application Programming Interface) defines how software systems communicate. **REST** (Representational State Transfer) is an architectural style for networked systems. A REST-style API commonly exposes resources through URLs and uses HTTP methods to act on those resources.

For example, an API for a collection of books might expose:

- `GET /books` — retrieve the collection
- `GET /books/42` — retrieve the book with ID `42`
- `POST /books` — create a book
- `PUT /books/42` — replace the representation of book `42`
- `PATCH /books/42` — partially update book `42`
- `DELETE /books/42` — delete book `42`

### Typical request and response

A client sends an HTTP request with a method, URL, headers, and—when needed—a body. The server validates and processes it, interacts with its data or other services, and returns an HTTP response with a status code, headers, and often a representation such as JSON.

Example request:

```http
GET /api/books/42 HTTP/1.1
Host: example.com
Accept: application/json
```

Possible response:

```http
HTTP/1.1 200 OK
Content-Type: application/json

{"id":42,"title":"Example"}
```

### Common REST principles and HTTP details

- **Resource-oriented:** URLs identify resources; HTTP methods express the intended operation.
- **Stateless requests:** Each request contains the information needed to process it. The server does not rely on stored conversational state from a previous request, although it may store application data and sessions separately.
- **Representations:** Resources are exchanged in formats such as JSON. A representation is not necessarily the resource's internal storage format.
- **HTTP semantics:** Methods and status codes communicate meaning. For example, `201 Created` indicates successful creation, `400 Bad Request` indicates an invalid request, `401 Unauthorized` indicates missing or invalid authentication credentials, `403 Forbidden` indicates the caller is not allowed, and `404 Not Found` indicates that the resource was not found.
- **Safety and idempotency:** `GET` is defined as safe (it should not request a state change). `PUT` and `DELETE` are defined as idempotent: repeating the same request has the same intended effect as making it once. `POST` is not generally idempotent.

Not every HTTP API is fully REST-compliant; “REST API” is often used informally for an API that uses HTTP, resource-like URLs, and JSON.

**Interview summary:** “A REST API lets clients interact with resources over HTTP. The client sends a request to a resource URL using a method such as GET or POST; the server processes it and returns a status code and usually a representation such as JSON. Statelessness and correct HTTP semantics are key REST principles.”

## 5. What is cloud computing? Explain IaaS, PaaS, and SaaS.

**Cloud computing** is the on-demand delivery of computing resources—such as servers, storage, databases, networking, and software—over a network, commonly the internet. Instead of purchasing and operating all infrastructure themselves, organizations can provision resources from a cloud provider and scale or pay for them according to a service model.

### The three common service models

| Model | What the provider supplies | What the customer typically manages | Example use |
|---|---|---|---|
| **IaaS — Infrastructure as a Service** | Virtualized compute, storage, and networking | Operating system, installed software, applications, and data | Provisioning virtual machines to host a custom application |
| **PaaS — Platform as a Service** | Infrastructure plus a managed application platform/runtime | Application code and data, plus configuration | Deploying an application without managing its servers or operating system |
| **SaaS — Software as a Service** | A complete, ready-to-use application | User settings, access, and the data they contribute | Using web-based email or a hosted collaboration tool |

### Comparing the levels

- **IaaS:** Offers the most control of these three models, but also leaves the customer with more operational responsibility. The customer configures and maintains the guest operating system and application stack.
- **PaaS:** The provider also manages much of the underlying platform and runtime. Developers can focus more on application code, while still managing application behavior and data.
- **SaaS:** The provider operates the application end to end. Customers use the software rather than deploying and maintaining its underlying platform.

The exact division of responsibility varies by provider and product. “Cloud” does not mean that security or maintenance is entirely handled by the provider; responsibilities are shared, and customers still need to configure access, protect data, and use services appropriately.

**Interview summary:** “Cloud computing provides computing resources on demand over a network. IaaS gives customers virtual infrastructure to manage, PaaS provides a managed platform for building and deploying applications, and SaaS delivers a complete application for customers to use.”