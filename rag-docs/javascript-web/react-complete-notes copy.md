---
title: REACT-COMPLETE-NOTES
topic: javascript-web
source_type: my-notes
source_file: STUDYNOTEs/REACT-COMPLETE-NOTES.md
---

# React.js — Complete Beginner-to-Advanced Notes


> Interview questions from these files live in a separate document: **REACT-INTERVIEW-QUESTIONS.md**

---

## How to read this document

Work through it top to bottom. Every part builds on the one before it.

| Part | What you learn | Read when |
|---|---|---|
| Part 1 | What React is and why it exists | Day 1 |
| Part 2 | Setting up your machine | Day 1 |
| Part 3 | JSX — writing HTML inside JavaScript | Day 2 |
| Part 4 | Components — the building blocks | Day 2–3 |
| Part 5 | Props — passing data down | Day 3 |
| Part 6 | State — data that changes | Day 4 |
| Part 7 | Hooks — the modern way (incl. all 17 hooks with examples) | Day 5–6 |
| Part 8 | Events — responding to the user | Day 7 |
| Part 9 | Conditional rendering, lists and keys | Day 8 |
| Part 10 | Forms | Day 9 |
| Part 11 | Styling | Day 10 |
| Part 12 | Fetching data from APIs | Day 11 |
| Part 13 | Routing — multiple pages | Day 12 |
| Part 14 | How React works inside (Virtual DOM, Fiber) | Day 13 |
| Part 15 | Build tools, bundlers, npm | Day 14 |
| Part 16 | Class components and lifecycle (legacy) | Day 15 |
| Part 17 | Refs, Fragments, Portals, HOCs, Context | Day 16–17 |
| Part 18 | State management — Context API, Redux, Flux | Day 18 |
| Part 19 | Performance optimization | Day 19 |
| Part 20 | Testing | Day 20 |
| Part 21 | Best practices, debugging, common mistakes | Day 21 |
| Part 22 | Building a real app (Food Villa walkthrough) | Day 22+ |
| Part 23 | React 19 — the modern APIs | After the basics |
| Part 24 | Quick reference sheets | Anytime |

---
---

# PART 1 — Introduction to React.js

## 1.1 What is React.js?

**React.js is an open-source JavaScript library used for building user interfaces (UIs).**

Break that sentence down, because every word matters:

- **Open-source** — free, and the code is public.
- **JavaScript library** — not a framework. This is an important distinction. A **library takes minimum effort to put into our code**; you call it when you want it. A framework tends to dictate the whole structure of your app.
- **User interfaces** — the visible part of an app: buttons, forms, lists, pages.

It was developed for the **view layer** of the application by **Facebook**. It was created by **Jordan Walke**, a software engineer at Facebook, and first released in **March 2013**.

React allows developers to create **reusable UI components** that efficiently update and render based on changes in data, providing a responsive and interactive user experience.

### Why is it called "react"?
Because it was designed to help developers **"react" to changes in the state of an application**, by efficiently rendering and updating the UI in response to those changes.

### Why do we use React?
The main objective of React is to develop a User Interface that **improves the speed of the app**. It uses a virtual DOM (a JavaScript object), which improves performance. The JavaScript virtual DOM is faster than the regular DOM. React can be used on the client and server-side, as well as with other frameworks. It uses component and data patterns that improve readability and help maintain larger apps.

---

## 1.2 The features of React (and why each one matters)

### 1. Virtual DOM
React uses a **virtual DOM** (Document Object Model) that efficiently updates and renders changes to the UI. The virtual DOM allows React to **minimize actual DOM manipulations**, leading to improved performance and a smoother user experience.

*Why it matters:* changing the real DOM directly is slow. React keeps a lightweight copy in memory, works out the smallest possible change, and only touches the real page where necessary.

### 2. Component-based architecture
React promotes the concept of **reusable components**, making it easier to build and maintain complex UIs. Components can be composed together, allowing for code reusability and modularity.

*Why it matters:* you write a `Button` once and use it in fifty places.

### 3. Declarative syntax
React follows a **declarative approach**, allowing developers to describe **how the UI should look based on its current state**. This makes it easier to understand and reason about the UI code.

*Why it matters:* you say *"when logged in, show the dashboard"* instead of writing step-by-step instructions to create, insert and remove DOM nodes.

### 4. Unidirectional (one-way) data flow
React implements a **unidirectional data flow**, where data flows in a **single direction from parent components to child components**. This makes it easier to track and debug data changes, reducing the likelihood of unexpected side effects.

*Why it matters:* when something is wrong, there is only one direction to look in.

### 5. React Native
React also provides **React Native**, a framework that allows developers to build mobile applications using React and JavaScript. With React Native, developers can create native mobile apps for both **iOS and Android** platforms using a **single codebase**.

### 6. JSX
JSX stands for **JavaScript XML**. It is a JavaScript syntax extension — an XML/HTML-like syntax used by React. This syntax is processed into JavaScript calls of the React Framework. It extends ES6 so that HTML-like text can co-exist with JavaScript React code. It is **not necessary** to use JSX, but it is recommended.

### 7. Simplicity
React uses JSX files which make the application simple to code and to understand. React is a component-based approach which makes the code reusable as you need. This makes it simple to use and learn.

### 8. Performance
React is known to be a great performer. The reason is that it manages the virtual DOM. The DOM is a cross-platform programming API which deals with HTML, XML or XHTML. The DOM exists entirely in memory. Because of this, when we create a component, we do not write directly to the DOM.

---

## 1.3 Advantages of React (the honest list)

1. **Easy to learn and use** — React is much easier to learn and use than many alternatives. It comes with a good supply of documentation, tutorials and training resources.
2. **Creating dynamic web applications becomes easier** — Creating a dynamic web app specifically with HTML strings was tricky because it required complex coding. React solves this and makes it easier. It provides less coding and gives more functionality. It makes use of JSX.
3. **Reusable components** — A React web app is made up of multiple components, each with its own logic and controls. These components output small, reusable code which helps make your apps easier to develop and maintain.
4. **Performance enhancement** — React improves performance due to the virtual DOM. Most developers faced problems when the DOM was updated, which slowed down application performance. React solved this problem by introducing the virtual DOM.
5. **The support of handy tools** — React has gained popularity partly due to a handy set of tools. **React Developer Tools** are designed as Chrome and Firefox dev extensions and allow you to inspect React component hierarchies in the virtual DOM.
6. **Known to be SEO friendly** — Traditional JavaScript frameworks have issues dealing with SEO. Search engines generally have trouble reading JS applications. React overcomes this problem, helping developers to be easily navigated on various search engines.
7. **The benefits of having a JavaScript library** — React offers a very rich JavaScript library. This provides more flexibility to web developers to choose the way they want to work.

## 1.4 Disadvantages of React (be aware of these)

1. **The high pace of development** — The environment continuously changes very fast, so some developers do not feel comfortable relearning new ways of doing things regularly.
2. **Poor documentation** — This is common for constantly updating technology. React accelerates so fast that documentation is not always kept properly up to date.
3. **View part only** — React covers only the UI layer of the app, nothing else. You still need to choose other technologies to get a complete tooling set for a development project.
4. **JSX is a barrier** — React uses JSX, a syntax extension that allows HTML mixed with JavaScript. Some members of the development community consider JSX a barrier, especially for new developers, and complain about its complexity in the learning curve.

---

## 1.5 React compared with other tools

### React vs AngularJS

| | AngularJS | ReactJS |
|---|---|---|
| Author | Google | Facebook community |
| Developer | Misko Hevery | Jordan Walke |
| Initial release | October 2010 | March 2013 |
| Version referenced | Angular 1.7.8 (11 March 2019) | React 16.8.6 (27 March 2019) |
| Language | JavaScript, HTML | JSX |
| Type | Open source MVC framework | Open source JS framework |
| Rendering | Client-side | Server-side |
| Packaging | Weak | Strong |
| Data binding | Bi-directional | Unidirectional |
| Testing | Unit and integration testing | Unit testing |
| App architecture | MVC | Flux |
| Dependencies | Manages dependencies automatically | Requires additional tools to manage dependencies |
| Routing | Requires a template or controller for router configuration, managed manually | Doesn't handle routing itself but has many modules for routing |
| Performance | Slow | Fast, due to virtual DOM |
| Best for | Single page applications that update a single view at a time | Single page applications that update multiple views at a time |

### React vs React Native

| | ReactJS | React Native |
|---|---|---|
| Initial release | 2013 | 2015 |
| Used for | Developing web applications | Developing mobile applications |
| Platform | Can be executed on all platforms | Not platform independent; takes more effort to run everywhere |
| Animation | Uses a JavaScript library and CSS for animations | Comes with built-in animation libraries |
| Navigation | Uses React-router for navigating web pages | Has its own navigation approach |
| Tags | Uses HTML tags | Does not use HTML tags |
| Reuse | Can reuse code components, saving valuable time | Can reuse React Native UI components and modules, allowing hybrid apps to render natively |
| Security | Provides high security | Provides lower security in comparison to ReactJS |

### React vs Vue

| | React | Vue |
|---|---|---|
| Definition | Declarative, efficient, flexible open-source JS library for building reusable UI components | Open-source JS library for building reusable user interfaces and single page applications |
| History | Created by Jordan Walke at Facebook; used in products like WhatsApp and Instagram | Created by Evan You, a former Google employee who worked on Angular projects. He wanted a better version of Angular — extracting the parts he liked and making it lighter |
| Preferred language | JavaScript / XML | HTML / JavaScript |
| Size | ~100 KB | ~60 KB |
| Performance | Slower compared to Vue | Faster compared to React |
| Flexibility | Great flexibility, supports third-party libraries | More limited flexibility compared to React |
| Version referenced | React 16.8.6 (27 March 2019) | Vue 2.6.10 (20 March 2019) |
| Long term support | Suitable for long term support | Not as suitable for long term support |

---
---

# PART 2 — Setting up a development environment

Follow these four steps in order.

### Step 1 — Install Node.js
React requires **Node.js**, so begin by installing the latest version from the official website (**http://nodejs.org**). Node.js comes with **npm** (Node Package Manager) which is used to manage project dependencies.

Check your versions in the terminal:
```bash
node -v
```
```bash
npm -v
```
You need **Node version ≥ 8.10** and **npm version ≥ 5.6**. (Example outputs: `v10.16.0` and `6.9.0`.)

### Step 2 — Create a new React project
Once Node.js is installed, create a new React project using the **Create React App (CRA)** command-line tool:
```bash
npx create-react-app my-react-app
```
This creates a folder called `my-react-app` with the basic structure and necessary files for a React project.

> **What is create-react-app?** It is an excellent tool for beginners which allows you to create and run a React project very quickly. It does not require any manual configuration. This tool wraps all of the required dependencies like Webpack and Babel for the React project itself, so you can focus on writing code. It is maintained by Facebook and works on macOS, Windows and Linux.

### Step 3 — Navigate into the project directory
```bash
cd my-react-app
```

### Step 4 — Start the development server
```bash
npm start
```
This starts the development server and launches your React application in a web browser. Any changes made to the code will **automatically trigger a hot reload**, allowing you to see the changes in real time.

---

## 2.1 The project folder structure

In a React application there are several files and folders in the root directory:

1. **`node_modules`** — Contains the React library and any other third-party libraries needed. This is where the "superpowers" come from. **Never edit this folder by hand.**
2. **`public`** — Holds the public assets of the application. It contains `index.html`, where React will mount the application by default on the `<div id="root"></div>` element.
3. **`src`** — Contains `App.css`, `App.js`, `index.js` and `serviceWorker.js`. The `App.js` file is always responsible for displaying the output screen in React.
4. **`package-lock.json`** — Generated automatically for any operation where npm modifies either the `node_modules` tree or `package.json`. It cannot be published. **It tells you the exact version of every library you are using.**
5. **`package.json`** — Holds various metadata required for the project. It gives information to npm, allowing it to identify the project and handle it.
6. **`README.md`** — Provides the documentation for the project.

### A very common real-world problem
> **Q: "Something works on my localhost / my machine but doesn't work in production. Why?"**
>
> **A:** The `package-lock.json` file tells the exact version of the library you are using. Suppose for a dev dependency you're using version 2.8.4 which is correct in `package-lock.json`, but in `package.json` it says `"^2.8.2"`. The `package-lock` file is the file that **locks** the version. Version drift between machines is the usual culprit.

### Why we don't put `node_modules` into git
Because `package-lock.json` has sufficient information to recreate `node_modules`. The lock file keeps and maintains the version of everything in `node_modules`.

The flow is:
```
node_modules on YOUR machine
        │
        │  (commit package-lock.json, NOT node_modules)
        ▼
       GIT
        │  (fetch)
        ▼
     SERVER  ──▶  regenerates node_modules from package-lock.json
```

Anything which can be auto-generated should be put inside `.gitignore` — that includes `node_modules` and `.parcel-cache`.

---
---

# PART 3 — JSX (JavaScript XML)

## 3.1 What is JSX?

**JSX is a syntax extension for JavaScript that allows us to write HTML-like code within JavaScript.**

It is a fundamental part of React.js and is used to define the **structure and appearance** of components. JSX combines the power of JavaScript with the simplicity and expressiveness of HTML-like syntax.

JSX allows you to write an HTML/XML-like structure in the **same file** where you write JavaScript code; then a preprocessor transforms these expressions into actual JavaScript code. Just like XML/HTML, JSX tags have a name, attributes, and children.

> **Critically important:** JSX **looks** similar to HTML, but JSX is **not actual HTML**. It is a syntax that gets transformed into JavaScript function calls by a transpiler like **Babel** before being executed by the browser.
>
> **JSX is not "HTML inside JavaScript". JSX has HTML-*like* syntax.**

### Why use JSX?
- It is **faster** than regular JavaScript because it performs optimization while translating the code to JavaScript.
- Instead of separating technologies by putting markup and logic in separate files, React uses components that contain both.
- It is **type-safe**, and most errors can be found at compilation time.
- It makes it **easier to create templates**.

### Advantages of JSX at a glance
- Better developer experience
- Syntactical sugar
- Readability
- Less code
- Maintainability
- No repetition

---

## 3.2 What JSX actually compiles to

This is the single most clarifying thing a beginner can learn.

**JSX file:**
```jsx
<div>Hello</div>
```

**What it becomes:**
```js
React.createElement("div", null, "Hello");
```

That line creates a React element by passing 3 arguments.

### The chain
```
JSX  ⇒  React.createElement()  ⇒  a plain JavaScript Object  ⇒  HTML (the real DOM)
```

**Babel converts JSX to `React.createElement()`.** Your browser cannot understand JSX; Babel understands it.

### Building without JSX (so you see what JSX saves you)

Take this HTML you want to produce:
```html
<div id="container">
  <h1 id="title">Heading 1</h1>
  <h2 id="title2">Heading 2</h2>
</div>
```

Written with `React.createElement`:
```js
const heading = React.createElement(
  "h1",                    // 1st argument: the TAG
  { id: "title" },         // 2nd argument: the ATTRIBUTES (these are "props")
  "Heading 1"              // 3rd argument: the CHILDREN
);

const heading2 = React.createElement(
  "h2",
  { id: "title2" },
  "Heading 2"
);

const container = React.createElement(
  "div",
  { id: "container" },
  [heading, heading2]      // children can be an array
);

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(container);
```

Now the same thing with JSX:
```jsx
const heading = <h1 id="title">Heading 1</h1>;
```

**"BUT, JSX makes life much easier."** If you have to build a big HTML structure, using `createElement()` is not a good solution — which is exactly why JSX was introduced.

> Note the second argument can contain anything you like:
> ```js
> { id: "container", hello: "world" }
> ```
> These are called **props**. Props can be anything.

---

## 3.3 Writing JSX expressions

In JSX, we can write expressions by embedding JavaScript code within **curly braces `{ }`**. This allows us to dynamically compute values and include them in our JSX.

```jsx
import React from 'react';

function Greeting() {
  const name = 'Alice';
  const age = 25;

  return (
    <div>
      <h1>Hello, {name}!</h1>
      <p>You are {age} years old.</p>
    </div>
  );
}

export default Greeting;
```

The expressions `{name}` and `{age}` get **evaluated** and their results are rendered in the resulting HTML.

> **Rule of thumb:** whenever you write JSX, you can write any piece of JavaScript code between curly braces `{ }` and it will work.

### JSX is secure
**JSX makes sure your app is safe. It does sanitization.** If you write `{data}` where `data` came from an API, JSX will sanitize the content before rendering it — which protects against injection attacks.

---

## 3.4 JSX attributes

JSX uses attributes with HTML elements, the same as regular HTML. But JSX uses **its own naming convention** rather than the standard HTML one:

- `class` in HTML becomes **`className`** in JSX — because `class` is a **reserved keyword in JavaScript**.
- For custom attributes, use the `data-` prefix.

```jsx
import React, { Component } from 'react';

class App extends Component {
  render() {
    return (
      <div>
        <h1>Javatpoint</h1>
        <h2>Training Institute</h2>
        <p data-demoAttribute="demo">This website contains the best CS tutorials</p>
      </div>
    );
  }
}

export default App;
```

### Attribute values can be specified in two ways

**1. As string literals** — values in double quotes:
```jsx
var element = <h2 className="firstAttribute">Hello Java</h2>
```

```jsx
class App extends Component {
  render() {
    return (
      <div>
        <h1 className="hello">Javatpoint</h1>
        <p data-demoAttribute="demo">This website contains topperworld info</p>
      </div>
    );
  }
}
```

**2. As expressions** — values inside curly braces:
```jsx
var element = <h2 className={varName}>Hello</h2>
```

```jsx
class App extends Component {
  render() {
    return (
      <div>
        <h1 className="hello">{25 + 20}</h1>
      </div>
    );
  }
}
```
Output: `45`

---

## 3.5 Static, dynamic and conditional attribute values

**Static attribute values** — assign a string or number directly:
```jsx
function MyComponent() {
  return <input type="text" disabled={true} />;
}
```
Here `type` has a static value of `"text"` and `disabled` has a static value of `true`.

**Dynamic attribute values** — use JavaScript expressions inside curly braces:
```jsx
function MyComponent() {
  const imageUrl = 'path/to/image.png';
  const altText = 'Image';
  return <img src={imageUrl} alt={altText} />;
}
```

**Conditional attribute values** — include or exclude based on conditions, using operators or ternary expressions:
```jsx
function MyComponent() {
  const isLoggedIn = true;
  return (
    <div>
      <h1>Welcome, {isLoggedIn ? 'User' : 'Guest'}!</h1>
      {isLoggedIn && <button>Logout</button>}
    </div>
  );
}
```
Here the heading text is chosen with a **ternary expression**, and the `button` element is conditionally rendered using the **logical AND operator (`&&`)**.

> JSX's ability to seamlessly integrate JavaScript within HTML-like syntax is one of the reasons React has become such a popular choice for building UIs.

---

## 3.6 Nested elements, comments and styling in JSX

### Nested elements
```jsx
import React, { Component } from 'react';

class App extends Component {
  render() {
    return (
      <div>
        <h1>Javatpoint</h1>
        <h2>Training Institute</h2>
        <p>This website contains the best CS tutorials</p>
      </div>
    );
  }
}

export default App;
```

### JSX comments
JSX allows comments that begin with `/*` and end with `*/`, wrapped in curly braces:
```jsx
{/* This is a comment in JSX */}
```

### JSX inline styling
React recommends using inline styles with **camelCase** syntax. React automatically appends `px` after number values on specific elements.

```jsx
import React, { Component } from 'react';

class App extends Component {
  render() {
    var myStyle = {
      fontSize: 80,
      fontFamily: 'Courier',
      color: '#003300'
    };
    return (
      <div>
        <h1 style={myStyle}>www.javatpoint.com</h1>
      </div>
    );
  }
}

export default App;
```

---
---

# PART 4 — Components

## 4.1 What is a component?

**In React, components are the building blocks of the user interface.**

A component is a **self-contained, reusable piece of code** that represents a part of the UI and **encapsulates its logic, state and rendering**.

Components allow developers to break down complex UI structures into smaller, manageable pieces, making the code easier to understand, maintain and reuse. Components can be **composed together** to create larger and more sophisticated UI structures.

> **"Everything is a component in React."**

React applications are made up of multiple components, and each component has its own logic and control. These components can be reusable, which helps you maintain the code when working on larger-scale projects.

---

## 4.2 The two types of component

```
                React Component
               /                \
    Functional Component     Class Component
       (the NEW way)            (the OLD way)
```

### Functional components — the modern default
A functional component is just a **plain JavaScript pure function** that accepts props as an argument and returns a React element (JSX).

```jsx
function WelcomeMessage(props) {
  return <h1>Welcome to the, {props.name}</h1>;
}
```

Or, as an arrow function:
```jsx
const HeaderComponent = () => {
  return <h1>Hello World</h1>;
};
```

The functional component is also known as a **stateless component** because, historically, they did not hold or manage state.

> **Convention:** for any component, the **name starts with a capital letter**. It is not strictly mandatory, but it is the convention and React relies on it to tell components apart from HTML tags.

### Class components — the legacy approach
Class components are more complex than functional components. They require you to **extend `React.Component`** and create a `render` function which returns a React element.

```jsx
import React from 'react';

class Welcome extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}!</h1>;
  }
}

export default Welcome;
```

In earlier versions of React, class components were the **primary** way to create components. Class components are JavaScript classes that extend the `React.Component` class and provide additional functionality, such as **lifecycle methods** and **local component state**.

**HOWEVER** — with the introduction of React hooks (in **React 16.8**), functional components became far more powerful and popular. Functional components are simpler, easier to read and encourage a more functional programming style. **Hooks allow functional components to have state and lifecycle behaviour that was previously only available in class components.**

---

## 4.3 Class vs Functional components — the full comparison

| Class Component | Functional Component |
|---|---|
| Requires you to extend from `React.Component` and create a `render` function that returns a React element | Just a plain JavaScript pure function that accepts props as an argument and returns a React element (JSX) |
| **Must** have `render()` returning JSX | There is **no** `render()` used |
| Also known as a **stateful** component | Also known as a **stateless** component |
| React lifecycle methods can be used inside (e.g. `componentDidMount`) | React lifecycle methods cannot be used |
| Requires different syntax inside the class to implement hooks | **Hooks can be easily used** to make them stateful |
| `constructor(props){ super(props); this.state = {name:''} }` | `const [name, setName] = React.useState('')` |
| Finally, a **class** | Finally, a **function** |

---

## 4.4 Creating and rendering components

**Class component example:**
```jsx
import React from 'react';

class Welcome extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}!</h1>;
  }
}

export default Welcome;
```

**Functional component example:**
```jsx
import React from 'react';

function Welcome(props) {
  return <h1>Hello, {props.name}!</h1>;
}

export default Welcome;
```

**To render a component**, import it into another component and include it in the JSX using angle brackets:
```jsx
import React from 'react';
import Welcome from './Welcome';

function App() {
  return (
    <div>
      <Welcome name="Alice" />
      <Welcome name="Bob" />
    </div>
  );
}

export default App;
```

In this example, the `Welcome` component is rendered **twice**, passing different names as props. This results in two separate instances of the `Welcome` component being rendered with the respective names.

---

## 4.5 React element vs Functional component

This distinction trips up almost every beginner.

| React element | Functional Component |
|---|---|
| `const heading = (<h1 id="title" key="h1">Hello World</h1>);` | `const heading = () => { return (<h1 id="title" key="h1">Hello World</h1>); };` |
| Is finally an **object** | Is finally a **function** |
| Rendered with `{heading}` | Rendered with `<Heading />` |

Turning the element into an arrow function that *returns* it makes it a functional component.

---

## 4.6 Component composition

**If you use a component inside another component, that is called component composition (or composing components).**

```jsx
const Title = () => {
  return <h1>Hello World</h1>;
};

const HeaderComponent = () => {
  return (
    <div>
      <Title />                  {/* component composition */}
      <h2>Namaste React</h2>
      <h2>Hai all</h2>
    </div>
  );
};
```

### Three ways to render a component
1. `{Title()}` — calling it as a plain function
2. `<Title />` — **used generally, this is the normal way**
3. `<Title></Title>` — the long form, needed when passing children

### Composing with a variable instead
```jsx
const title = (<h1>Hello world</h1>);   // a normal variable holding an element

const HeaderComponent = () => {
  return (
    <div>
      {title}                          {/* rendered with curly braces */}
      <h2>Namaste React</h2>
    </div>
  );
};
```

---

## 4.7 Two important rules

> **Never create a component inside a component.** You can *compose* components, but do not define one inside the body of another — React will re-create it on every render and destroy its state.

> **Never write a `useState` inside an `if...else` or a `for` loop.** Hooks must be called at the top level. See Part 7 for the full Rules of Hooks.

---

## 4.8 A worked multi-component example

```jsx
import React, { Component } from 'react';

class App extends React.Component {
  render() {
    return (
      <div>
        <First />
        <Second />
      </div>
    );
  }
}

class First extends React.Component {
  render() {
    return (
      <div>
        <h1>JavaTPoint</h1>
      </div>
    );
  }
}

class Second extends React.Component {
  render() {
    return (
      <div>
        <h2>www.javatpoint.com</h2>
        <p>This website contains the great CS tutorials</p>
      </div>
    );
  }
}

export default App;
```
Output:
```
JavaTpoint
www.javatpoint.com
This website contains the great CS tutorial.
```

---
---

# PART 5 — Props

## 5.1 What are props?

**"Props" is short for "properties".** They are a way to **pass data from one React component to another** — specifically, from a **parent** component down to its **child** components.

Props allow you to make your components **dynamic and reusable** by supplying different data to them.

Key facts:
- Props are an **object** which stores the value of the attributes of a tag, and works similarly to HTML attributes.
- Props are **read-only**. They are **immutable** — we cannot modify props from inside the component that receives them.
- Props are passed as attributes when rendering a component.

---

## 5.2 Declaring, passing and accessing props

### Declaring
```jsx
// Functional component
function MyComponent(props) {
  return <div>{props.message}</div>;
}

// Class component
class MyComponent extends React.Component {
  render() {
    return <div>{this.props.message}</div>;
  }
}
```

### Passing
Specify the prop as an attribute when using the component:
```jsx
<MyComponent message="Hello, world" />
```

### Accessing
Inside the receiving component, access the prop like a variable:
- In a **functional** component, it comes in as a parameter: `props.message`
- In a **class** component, use `this.props.message`

### A full example
```jsx
import React from 'react';

function Greeting(props) {
  return <h1>Hello, {props.name}!</h1>;
}

function App() {
  return <Greeting name="Alice" />;
}

export default App;
```
The `Greeting` component receives the `name` prop from its parent component `App`. The value is accessed using `props.name`.

---

## 5.3 Using props dynamically

Props can be used dynamically, allowing your components to display different data based on what's passed to them:
```jsx
<MyComponent message="Hello world" />
<MyComponent message="Welcome" />
```

---

## 5.4 Default props

You can set default values for props using `defaultProps`. If a prop is not provided, the default value will be used.

```jsx
MyComponent.defaultProps = {
  message: "Default Message"
};
```

Full example:
```jsx
import React, { Component } from 'react';

class App extends React.Component {
  render() {
    return (
      <div>
        <h1>Default Props Example</h1>
        <h3>Welcome to {this.props.name}</h3>
        <p>Javatpoint is one of the best training institutes in India</p>
      </div>
    );
  }
}

App.defaultProps = {
  name: "JavaTpoint"
};

export default App;
```

---

## 5.5 Props validation (PropTypes)

Props are an important mechanism for passing read-only attributes to a React component, and they usually need to be used correctly. `propTypes` is used for props validation. When props are passed with an invalid type, you get warnings in the JavaScript console.

Syntax:
```jsx
class App extends React.Component {
  render() { /* ... */ }
}

App.propTypes = {
  /* validators go here */
};
```

### The prop type validators

| Prop Type | Description |
|---|---|
| `PropTypes.any` | The prop can be of any data type |
| `PropTypes.array` | The prop should be an array |
| `PropTypes.bool` | The prop should be a boolean |
| `PropTypes.func` | The prop should be a function |
| `PropTypes.number` | The prop should be a number |
| `PropTypes.object` | The prop should be an object |
| `PropTypes.string` | The prop should be a string |
| `PropTypes.symbol` | The prop should be a Symbol |
| `PropTypes.instanceOf` | The prop should be an instance of a particular JavaScript class |
| `PropTypes.isRequired` | The prop **must** be provided |
| `PropTypes.element` | The prop must be an element |
| `PropTypes.node` | The prop can render anything: number, string, element, or an array of these |
| `PropTypes.oneOf()` | The prop should be one of several specific values |
| `PropTypes.oneOfType([PropTypes.string, PropTypes.number])` | The prop should be an object that could be one of many types |

### Custom validators
React allows creating a custom validation function. The function receives these arguments:
- **props** — the first argument
- **propName** — the name of the prop being validated
- **componentName** — the name of the component being validated

```jsx
var Component = React.createClass({
  App.propTypes = {
    customProp: function(props, propName, componentName) {
      if (!item.isValid(props[propName])) {
        return new Error('Validation failed');
      }
    }
  }
});
```

---

## 5.6 The `children` prop

The **children prop** is a special prop that is used to pass child elements to a component. It is used to pass elements between components, such as a list of items or a set of nested components.

```jsx
function Panel({ children }) {
  return <div className="panel">{children}</div>;
}
```
Usage:
```jsx
<Panel>
  <h1>Anything in here</h1>
  <p>becomes `children`</p>
</Panel>
```
**Best practice:** this enables flexible composition without prop explosion.

---

## 5.7 Object destructuring and the spread operator with props

These two JavaScript features make working with props dramatically cleaner.

### Object destructuring
Instead of `props.restaurant.data.name` everywhere, pull the values out:
```jsx
const RestaurantCard = (props) => {
  const { name, cuisines, cloudinaryImgId, time } = props.restaurant.data;
  // now just use {name}, {cuisines} etc.
};
```

Or destructure right in the parameter list:
```jsx
const RestaurantCard = ({ name, cuisines, cloudinaryImgId, time }) => {
  return (
    <div className="card">
      <img src={"https://some-cdn-url/" + cloudinaryImgId} />
      <h2>{name}</h2>
      <h3>{cuisines.join(", ")}</h3>
      <h4>{time} minutes</h4>
    </div>
  );
};
```

### The spread operator `...`
The spread operator is denoted by **three dots (`...`)**. It allows an iterable (an object that can be looped over, such as an array or a string) to be **expanded in places where multiple elements are expected**.

Instead of writing out every single prop:
```jsx
<RestaurantCard
  name={restaurantList[0].data.name}
  cuisines={restaurantList[0].data.cuisines}
  time={restaurantList[0].data.time}
  // ...and ten more
/>
```
just spread the object:
```jsx
<RestaurantCard {...restaurantList[0].data} />
```

---

## 5.8 Optional chaining `?.`

**Optional chaining allows us to access an object's properties without having to check whether the object or its properties exist.**

- Represented by **`?.`**
- A feature introduced in JavaScript **ES2020**

```jsx
<h2>{restaurantList[0].data?.name}</h2>
<h3>{restaurantList[0].data?.cuisines.join(", ")}</h3>
```

If `data` is `undefined`, this returns `undefined` instead of throwing an error and crashing your app. When you are fetching data from an API and the data hasn't arrived yet, this saves you constantly.

---
---

# PART 6 — State

## 6.1 What is state?

**State is an updatable structure used to contain data or information about a component.**

State refers to the **internal data of a component**. It represents the dynamic values that can change over time and affect the rendering and behaviour of the component. State is typically used to store and manage data that is **specific to a particular component**.

- The state in a component **can change over time**.
- The change in state can happen as a response to a **user action** or a **system event**.
- A component with state is known as a **stateful component**.
- It can be set by using `setState()`, and calling `setState()` **triggers a UI update**.
- It can only be accessed or modified **inside the component**.
- **A state must be kept as simple as possible.**

> If we have five components that need data or information from the state, then we should create one **container component** that will keep the state for all of them.

---

## 6.2 State in a class component

To define state, first declare a default set of values for the component's initial state. Add a **constructor** which assigns the initial state using `this.state`. It can then be rendered inside `render()`.

```jsx
import React from 'react';

class Counter extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      count: 0,
    };
  }

  incrementCount() {
    this.setState({ count: this.state.count + 1 });
  }

  render() {
    return (
      <div>
        <p>Count: {this.state.count}</p>
        <button onClick={() => this.incrementCount()}>
          Increment
        </button>
      </div>
    );
  }
}

export default Counter;
```

The `Counter` component has a `count` state variable initialised to `0` in the constructor. The `incrementCount` method updates the `count` state using the `setState` method, triggering a **re-render** of the component.

> **To set the state it is required to call `super()` in the constructor.** This is because `this.state` is initialised before `super()` has been called.

### Another example with conditional display
```jsx
import React from 'react';

class App extends React.Component {
  constructor() {
    super();
    this.state = { displayBio: true };
  }

  render() {
    const bio = this.state.displayBio ? (
      <div>
        <p><h3>Welcome</h3></p>
      </div>
    ) : null;

    return (
      <div>
        <h1>Hello</h1>
        {bio}
      </div>
    );
  }
}

export default App;
```

### Changing state with a toggle
We change the component state using `setState()` and passing a new state object as the argument.

```jsx
import React, { Component } from 'react';

class App extends React.Component {
  constructor() {
    super();
    this.state = { displayBio: false };
    this.toggleDisplayBio = this.toggleDisplayBio.bind(this);
  }

  toggleDisplayBio() {
    this.setState({ displayBio: !this.state.displayBio });
  }

  render() {
    return (
      <div>
        <h1>Welcome to Javatpoint</h1>
        {
          this.state.displayBio ? (
            <div>
              <h4>JavaTpoint is one of the best Java institutes in Noida</h4>
              <button onClick={this.toggleDisplayBio}>Show Less</button>
            </div>
          ) : (
            <div>
              <button onClick={this.toggleDisplayBio}>Read more</button>
            </div>
          )
        }
      </div>
    );
  }
}

export default App;
```

---

## 6.3 State in a functional component — `useState`

This is the modern way, and what you should learn first.

```jsx
import React, { useState } from 'react';

function CountApp() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>
        Click me
      </button>
    </div>
  );
}

export default CountApp;
```

Full explanation of the pattern in Part 7.

---

## 6.4 State and props working together

It is possible to combine both state and props. You can set the state in the **parent** component and pass it to the **child** component using props.

**App.js**
```jsx
import React, { Component } from 'react';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      name: "TopperWorld"
    };
  }

  render() {
    return (
      <div>
        <JTP jtpProp={this.state.name} />
      </div>
    );
  }
}

class JTP extends React.Component {
  render() {
    return (
      <div>
        <h1>State & Props example</h1>
        <h3>Welcome to {this.props.jtpProp}</h3>
        <p>ReactJS handwritten notes from TopperWorld</p>
      </div>
    );
  }
}

export default App;
```

**main.js**
```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App.js';

ReactDOM.render(<App />, document.getElementById('app'));
```

Output:
```
State & Props Example
Welcome to TopperWorld
ReactJS handwritten notes from TopperWorld
```

---

## 6.5 State vs Props — the critical comparison

| State | Props |
|---|---|
| State changes can be **asynchronous** | Props are **read-only** |
| State is **mutable** | Props are **immutable** |
| State **cannot** be accessed by child components | Props **can** be accessed by child components |
| A stateless component **cannot** have state | Stateless components **can** have props |
| State **cannot** make a component reusable | Props **can** make a component reusable |
| State is **internal** and controlled by the React component itself | Props are **external** and controlled by whatever renders the component |
| Holds information about the component | Used to pass data from one component to another as an argument |
| Can be used for rendering dynamic changes within a component | Used to communicate between components |
| Contains default values | Also contains default values |

### What they have in common
1. Both are plain JavaScript objects.
2. Both can contain default values.
3. Both are read-only when accessed via `this.`

---

## 6.6 Updating state and props correctly

### State
To update the state of a component, you should use the `setState` method (class) or the setter from `useState` (function). It is important to remember that:
- **State updates are asynchronous** and may be **batched together** for performance reasons.
- When updating state, it is recommended to use the **callback form** to ensure you're working with the latest state values.

```jsx
// Class component — callback form
this.setState((prevState) => ({
  count: prevState.count + 1,
}));
```

```jsx
// Functional component — callback form
setCount(prev => prev + 1);
```

> **Why must we pass a function to `setState()`?**
> Because `setState()` is asynchronous — it batches multiple calls together and only updates the component once. By passing a function, we guarantee the latest state is used when the component re-renders.

### Props
Props are passed down from parent components and are **read-only** within the child. To update props, you need to **modify the value in the parent component** and pass the updated value down. The child component will automatically re-render with the updated props.

In most cases, props pass data from a parent to its children; if you need to modify the data, you should manage it in the **parent component's state**.

> **Important:** updating state or props will trigger a **re-rendering** of the component and its child components to reflect the updated data. Carefully manage and update state and props to ensure the desired behaviour and performance.

### Never mutate state directly

| ❌ DON'T | ✅ DO |
|---|---|
| `state.items.push(x); setState(state)` | `setState({ ...state, items: [...state.items, x] })` |

**State mutation** is when the current state is modified directly instead of creating a new state object. This makes it difficult to track changes and can lead to unexpected behaviour. To prevent it, use the **spread operator** or **`Object.assign()`** to create a new state object and only update the properties that need to change.

---

## 6.7 One-way vs two-way data binding

Consider a search input:
```jsx
const Body = () => {
  const searchTxt = "KFC";
  return (
    <div>
      <input type="text" placeholder="Search" value={searchTxt} />
    </div>
  );
};
```
The value "KFC" goes into the input box, but **you cannot type in it**. Why? Because it is a hardcoded value. To change what's in the box, you must change the variable `searchTxt` — but typing doesn't change it.

**This is one-way data binding.**

To fix it, add an `onChange` handler *and* make `searchTxt` a state variable:

```jsx
const Body = () => {
  const [searchTxt, setSearchTxt] = useState("KFC");

  return (
    <div className="search-container">
      <input
        type="text"
        className="search-input"
        placeholder="Search"
        value={searchTxt}                       // reading
        onChange={(e) => {
          setSearchTxt(e.target.value);         // writing
        }}
      />
      <button className="search-btn">
        Search - {searchTxt}
      </button>
    </div>
  );
};
```

Now you are both **reading and writing** `searchTxt`. **This is two-way binding.**

### Why do we need state variables at all — why not just local variables?
**Because React has no idea what's happening to your local variables.** React won't re-render when a plain variable changes. Every time the variable needs to be in sync with the UI, it must be a **state variable**. **React keeps track of state variables.**

Whenever a state variable is updated, the whole component **re-renders** — React destroys the component and creates it again — with reconciliation (the diff algorithm) happening behind the scenes. But it only actually re-renders the changed portion, so it is very quick.

---
---

# PART 7 — React Hooks

## 7.1 What are hooks?

**Hooks are the new feature introduced in React 16.8 (2019). They allow you to use state and other React features without writing a class.**

Hooks are **normal JavaScript functions**. You import them from the `react` library using named imports.

With functional components, React introduced hooks, which are functions that allow functional components to use **state and lifecycle features**. Hooks enable functional components to achieve the same functionality as class components, but in a **more concise and declarative manner**.

---

## 7.2 The Rules of Hooks

There are two hard rules. Breaking them causes bugs that are very hard to trace.

1. **Only call hooks at the top level.** Never call hooks inside loops, conditions, or nested functions.
2. **Only call hooks from React functions.** Call them from React functional components or from your own custom hooks — not from regular JavaScript functions.

> Corollary: **never write a `useState` inside an `if..else` or a `for` loop.**
> `useState` is a hook React gives you to create a local state variable inside a functional component — so never use `useState` outside a functional component either (it wouldn't make sense).

There is an ESLint plugin for hooks: a set of rules that enforces the rules of hooks as specified by the React team. It helps prevent common mistakes and inconsistencies, and makes sure hooks are only used in functional components and called in the correct order.

---

## 7.3 The eleven core hooks

> Every hook below — plus `useDeferredValue`, `useSyncExternalStore` and `useInsertionEffect` — has a full working example in **section 7.6**.

### `useState` — local component state
```jsx
const [n, setN] = useState(0);
setN(n + 1);
setN(p => p + 1);      // callback form — safer
```
> ⚠️ Updates are **batched & async** — don't read state right after setting it.

**How it works:**
- `useState()` is a function that **returns an array**.
- The **first element** is the state variable itself.
- The **second element** is a **setter function** used to update it.
- The argument you pass is the **initial value**.

```jsx
const [searchTxt, setSearchTxt] = useState("KFC");
//     ^ variable  ^ setter fn            ^ initial value
```

Compare to plain JavaScript, where you would just write `const searchTxt = "KFC";`. In React, to modify the variable you *must* use the setter function that `useState` gives you.

**Full example:**
```jsx
const [title, setTitle] = useState("hi");

return (
  <div>
    <h1>{title}</h1>
    <button onClick={() => setTitle("New Food App")}>
      Change Title
    </button>
  </div>
);
```
React keeps track of the state variable `title` once it is created. On click of the button, the title gets updated from `"hi"` to `"New food app"`. The whole UI re-renders and updates quickly.

---

### `useEffect` — sync with an external system after render
```jsx
useEffect(() => {
  const id = setInterval(tick, 1000);
  return () => clearInterval(id);      // cleanup function
}, []);
```
> ⚠️ **Common mistake:** a missing or incorrect dependency array causes **stale closures**.

**How it works:**
```jsx
useEffect(callbackFunction, dependencyArray)
```
- The **callback function** is not called immediately — React calls it whenever `useEffect` wants it called, at a specific time.
- Whenever the component renders and re-renders, first the component's own code runs, and **after every render** React calls the callback function passed to `useEffect`.

**There are 2 ways a component re-renders:**
1. State change
2. Props change

**The role of the dependency array:**

| Dependency array | When the callback runs |
|---|---|
| *(omitted entirely)* | After **every** render — usually a bad idea |
| `[]` (empty) | **Only once**, after the initial render |
| `[searchTxt]` | Whenever `searchTxt` changes |
| `[count, count2]` | Whenever `count` **or** `count2` changes |

```jsx
useEffect(() => {
  console.log("call this when the dependency changes");
}, [searchTxt]);
```

**The cleanup function:** `useEffect` can return a function. React runs it before the next effect and when the component unmounts. Use it to remove event listeners, clear intervals, cancel subscriptions.

```jsx
useEffect(() => {
  // side effect code here
  return () => {
    // cleanup code here
  };
}, [dependency]);
```

**Example: sync the document title**
```jsx
import React, { useState, useEffect } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    document.title = `count: ${count}`;
  }, [count]);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>
        Increment
      </button>
    </div>
  );
}

export default Counter;
```

> You can use **more than one `useEffect`** in a single component, according to your use case. That is often cleaner than cramming unrelated logic into one.

---

### `useContext` — read a context value without prop drilling
```jsx
const theme = useContext(ThemeCtx);
```
> ⚠️ Re-renders on **any** context value change — split contexts to limit the blast radius.

---

### `useReducer` — state transitions via actions
```jsx
const [s, dispatch] = useReducer(reducer, init);
dispatch({ type: 'inc' });
```
> Prefer over `useState` when the next state depends on multiple sub-values.

---

### `useRef` — a mutable value that persists without re-rendering
```jsx
const ref = useRef(null);
<input ref={ref} />
```
> ⚠️ **Mutating `ref.current` does NOT trigger a re-render.** That is the whole point of it.

---

### `useMemo` — memoize an expensive computed value
```jsx
const sorted = useMemo(
  () => data.slice().sort(cmp),
  [data]
);
```
> ⚠️ Not a guarantee — React may discard the cache under memory pressure.

---

### `useCallback` — memoize a function identity across renders
```jsx
const onClick = useCallback(
  () => save(id), [id]
);
```
> Only useful when passed to **memoized children** or used in **effect dependencies**.

---

### `useLayoutEffect` — like `useEffect`, but fires synchronously before paint
```jsx
useLayoutEffect(() => {
  el.current.style.left = measure();
});
```
> ⚠️ **Blocks the browser paint** — use only for layout reads/writes.

---

### `useImperativeHandle` — customize the instance exposed via ref
```jsx
useImperativeHandle(ref, () => ({
  focus: () => input.current.focus()
}));
```
> Pairs with ref-as-prop in React 19 — `forwardRef` is no longer required.

---

### `useDebugValue` — label a custom hook's value in React DevTools
```jsx
useDebugValue(isOnline ? 'Online' : 'Offline');
```
> Dev-only utility — has zero effect on production behavior.

---

### `useId` — generate a stable, unique ID for accessibility attributes
```jsx
const id = useId();
<label htmlFor={id}>Name</label>
<input id={id} />
```
> ⚠️ **Do not use as a React key in a list** — it's for a11y IDs only.

---

## 7.4 `useRef` in depth

`useRef` returns a ref object whose `current` property is initialized to the passed argument.

```jsx
const refContainer = useRef(initialValue);
```

**Focusing an input:**
```jsx
function useRefExample() {
  const inputRef = useRef(null);

  const onButtonClick = () => {
    inputRef.current.focus();
  };

  return (
    <>
      <input ref={inputRef} type="text" />
      <button onClick={onButtonClick}>Submit</button>
    </>
  );
}
```

**Setting a value directly:**
```jsx
import React, { useRef } from 'react';

function MyComponent() {
  const inputRef = useRef(null);

  function handleClick() {
    inputRef.current.value = "Hello World!";
  }

  return (
    <div>
      <input type="text" ref={inputRef} />
      <button onClick={handleClick}>Update Input</button>
    </div>
  );
}

export default MyComponent;
```

---

## 7.5 Custom hooks

**Yes, you can create your own React hooks.** Follow the naming convention of starting the name with **"use"**, and use state and other hooks inside it.

```jsx
function useToggle(init = false) {
  const [v, set] = useState(init);
  return [v, () => set(x => !x)];
}
```

**What to keep in mind when creating custom hooks:**
- They should only call other hooks **at the top level**, not inside loops or conditions.
- Make sure the hook only performs **one specific action**.

**Best practice:** extract reusable stateful logic into a custom hook; prefix with `use`.

---

## 7.6 The complete hook reference — all 17 hooks with working examples

*Source: `reacthooks.pdf` — "React Hooks, 2026 Edition: A complete, up-to-date guide to every React hook, from the essentials to the newest React 19 additions" (@MohitDecodes, mohitdecodes.com).*

This section gives a full, runnable example for **every** hook React ships. Use it as your lookup table once you understand the concepts in 7.1–7.5.

| # | Hook | Category |
|---|---|---|
| 1 | `useState` | State |
| 2 | `useEffect` | Side effects |
| 3 | `useContext` | Global state |
| 4 | `useRef` | DOM & mutable values |
| 5 | `useReducer` | Complex state |
| 6 | `useMemo` | Performance |
| 7 | `useCallback` | Performance |
| 8 | `useLayoutEffect` | DOM timing |
| 9 | `useImperativeHandle` | Ref customization |
| 10 | `useDebugValue` | DevTools |
| 11 | `useId` | Accessibility |
| 12 | `useTransition` | Concurrent UI |
| 13 | `useDeferredValue` | Concurrent UI |
| 14 | `useSyncExternalStore` | External stores |
| 15 | `useInsertionEffect` | CSS-in-JS |
| 16 | `useActionState` | React 19 · Forms |
| 17 | `use` | React 19 · Suspense |

---

### 1. `useState` — Managing State in Functional Components

**`useState` lets you add state to function components. It returns a stateful value and a function to update it.**

```jsx
import { useState } from "react";

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>
        Increment
      </button>
    </div>
  );
}
```

---

### 2. `useEffect` — Handling Side Effects in React

**`useEffect` runs side effects like fetching data, subscriptions, or manual DOM manipulations after render.**

```jsx
import { useEffect, useState } from "react";

function FetchData() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch("/api/todos/1")
      .then((res) => res.json())
      .then((json) => setData(json));
  }, []);

  return <pre>{JSON.stringify(data, null, 2)}</pre>;
}
```

---

### 3. `useContext` — Accessing Global State with Context

**`useContext` lets you read and subscribe to values from React Context without prop drilling.**

```jsx
import { createContext, useContext } from "react";

const ThemeContext = createContext("light");

function ThemedButton() {
  const theme = useContext(ThemeContext);
  const bg = theme === "dark" ? "#333" : "#fff";

  return (
    <button style={{ background: bg }}>
      Click Me
    </button>
  );
}

function App() {
  return (
    <ThemeContext.Provider value="dark">
      <ThemedButton />
    </ThemeContext.Provider>
  );
}
```

---

### 4. `useRef` — Managing DOM References and Preserving Values

**`useRef` creates a mutable object that persists across renders without causing re-renders.**

```jsx
import { useRef } from "react";

function FocusInput() {
  const inputRef = useRef(null);

  return (
    <div>
      <input ref={inputRef} />
      <button onClick={() => inputRef.current.focus()}>
        Focus
      </button>
    </div>
  );
}
```

---

### 5. `useReducer` — State Management with Reducers

**`useReducer` is an alternative to `useState` for complex state logic, updating state via dispatched actions.**

```jsx
import { useReducer } from "react";

function reducer(state, action) {
  switch (action.type) {
    case "increment":
      return { count: state.count + 1 };
    case "decrement":
      return { count: state.count - 1 };
    default:
      return state;
  }
}

function Counter() {
  const [state, dispatch] = useReducer(reducer, { count: 0 });

  return (
    <div>
      <p>Count: {state.count}</p>
      <button onClick={() => dispatch({ type: "increment" })}>
        +
      </button>
      <button onClick={() => dispatch({ type: "decrement" })}>
        -
      </button>
    </div>
  );
}
```

---

### 6. `useMemo` — Optimizing Performance with Memoization

**`useMemo` caches the result of an expensive calculation between renders, recomputing only when dependencies change.**

```jsx
import { useMemo, useState } from "react";

function ExpensiveCalculation({ num }) {
  const squared = useMemo(() => {
    console.log("Calculating...");
    return num * num;
  }, [num]);

  return <p>Squared: {squared}</p>;
}

function App() {
  const [num, setNum] = useState(2);

  return (
    <div>
      <ExpensiveCalculation num={num} />
      <button onClick={() => setNum(num + 1)}>Increase</button>
    </div>
  );
}
```

> Note the `console.log` — it only fires when `num` actually changes, not on every render of `App`.

---

### 7. `useCallback` — Memoizing Functions to Prevent Unnecessary Re-Renders

**`useCallback` memoizes a function definition so it isn't recreated on every render, avoiding unnecessary child re-renders.**

```jsx
import { useState, useCallback } from "react";

function Button({ handleClick }) {
  return <button onClick={handleClick}>Click Me</button>;
}

function App() {
  const [count, setCount] = useState(0);

  const increment = useCallback(() => {
    setCount((prev) => prev + 1);
  }, []);

  return (
    <div>
      <p>Count: {count}</p>
      <Button handleClick={increment} />
    </div>
  );
}
```

> The empty dependency array works here because `setCount` uses the **callback form** `(prev) => prev + 1`, so the function never needs to close over the current `count`.

---

### 8. `useLayoutEffect` — Syncing with the DOM Before Paint

**`useLayoutEffect` runs synchronously after DOM mutations but before the browser repaints the screen.**

```jsx
import { useLayoutEffect, useRef } from "react";

function Box() {
  const boxRef = useRef(null);

  useLayoutEffect(() => {
    boxRef.current.style.transform = "scale(1.2)";
  }, []);

  const style = { width: 100, height: 100, background: "blue" };

  return <div ref={boxRef} style={style} />;
}
```

> Because it runs before paint, the user never sees the un-scaled box flash. With `useEffect` they might.

---

### 9. `useImperativeHandle` — Customizing the Instance Value Exposed to Parents

**`useImperativeHandle` customizes the value exposed to parent components when using ref forwarding.**

```jsx
import { forwardRef, useImperativeHandle, useRef } from "react";

const CustomInput = forwardRef((_, ref) => {
  const inputRef = useRef();

  useImperativeHandle(ref, () => ({
    focus: () => inputRef.current.focus(),
  }));

  return <input ref={inputRef} />;
});

function App() {
  const inputRef = useRef();

  return (
    <div>
      <CustomInput ref={inputRef} />
      <button onClick={() => inputRef.current.focus()}>
        Focus Input
      </button>
    </div>
  );
}
```

> The parent gets **only** the `focus` method — not the whole DOM node. That is the point: you control the surface area you expose.

---

### 10. `useDebugValue` — Debugging Custom Hooks

**`useDebugValue` displays a readable label for a custom hook inside React DevTools, making debugging easier.**

```jsx
import { useState, useDebugValue } from "react";

function useCustomHook(value) {
  const [state, setState] = useState(value);
  useDebugValue(state > 5 ? "High" : "Low");
  return [state, setState];
}

function App() {
  const [count, setCount] = useCustomHook(3);

  return (
    <button onClick={() => setCount(count + 1)}>
      Count: {count}
    </button>
  );
}
```

---

### 11. `useId` — Generating Stable Unique IDs

**`useId` generates stable, unique IDs for form elements, useful for accessibility attributes like `htmlFor`.**

```jsx
import { useId } from "react";

function Form() {
  const id = useId();

  return (
    <div>
      <label htmlFor={id}>Name:</label>
      <input id={id} type="text" />
    </div>
  );
}
```

---

### 12. `useTransition` — Marking Non-Urgent State Updates

**`useTransition` lets you mark a state update as a non-blocking transition, keeping the UI responsive during heavy renders.**

```jsx
import { useState, useTransition } from "react";

function SearchList() {
  const [isPending, startTransition] = useTransition();
  const [query, setQuery] = useState("");

  function handleChange(e) {
    const value = e.target.value;
    startTransition(() => setQuery(value));
  }

  return (
    <div>
      <input onChange={handleChange} />
      {isPending && <p>Loading...</p>}
      <List query={query} />
    </div>
  );
}
```

---

### 13. `useDeferredValue` — Deferring Non-Critical Updates

**`useDeferredValue` lets a part of the UI show stale content briefly while fresher, more urgent content renders first.**

```jsx
import { useState, useDeferredValue } from "react";

function Search() {
  const [text, setText] = useState("");
  const deferredText = useDeferredValue(text);

  function handleChange(e) {
    setText(e.target.value);
  }

  return (
    <div>
      <input value={text} onChange={handleChange} />
      <Results query={deferredText} />
    </div>
  );
}
```

> **`useTransition` vs `useDeferredValue`:** `useTransition` wraps the *update* you are causing. `useDeferredValue` wraps a *value* you are receiving. Reach for `useDeferredValue` when you don't control the state setter — for example when the value arrives as a prop.

---

### 14. `useSyncExternalStore` — Subscribing to External Data Sources

**`useSyncExternalStore` lets components safely read and subscribe to state that lives outside React, like browser APIs.**

```jsx
import { useSyncExternalStore } from "react";

function subscribe(callback) {
  window.addEventListener("online", callback);
  window.addEventListener("offline", callback);
  return () => {
    window.removeEventListener("online", callback);
    window.removeEventListener("offline", callback);
  };
}

function getSnapshot() {
  return navigator.onLine;
}

function useOnlineStatus() {
  return useSyncExternalStore(subscribe, getSnapshot);
}
```

> This is the correct, tear-free way to read external mutable state. It is what state libraries like Redux and Zustand use internally.

---

### 15. `useInsertionEffect` — Injecting Styles Before Layout

**`useInsertionEffect` fires before any DOM mutations are read, mainly built for CSS-in-JS libraries to inject styles.**

```jsx
import { useInsertionEffect } from "react";

function useCSSRule(rule) {
  useInsertionEffect(() => {
    const style = document.createElement("style");
    style.textContent = rule;
    document.head.appendChild(style);
    return () => document.head.removeChild(style);
  }, [rule]);
}
```

> You will almost certainly never call this in application code. It exists so that libraries like styled-components can insert styles at exactly the right moment. **Know it for interviews; don't reach for it in a feature.**

---

### 16. `useActionState` — Managing State Driven by Form Actions *(React 19)*

**`useActionState` manages state updated by a form action, and exposes a pending flag while the action is running.**

```jsx
import { useActionState } from "react";

async function submitForm(prevState, formData) {
  const name = formData.get("name");
  return { message: `Hello, ${name}!` };
}

function NameForm() {
  const [state, formAction, isPending] =
    useActionState(submitForm, { message: "" });

  return (
    <form action={formAction}>
      <input name="name" />
      <button type="submit" disabled={isPending}>
        Submit
      </button>
      <p>{state.message}</p>
    </form>
  );
}
```

---

### 17. `use` — Reading Resources Directly During Render *(React 19)*

**The `use` API lets you read the value of a promise or context directly in render, and works great with Suspense.**

```jsx
import { use, Suspense } from "react";

function Comments({ commentsPromise }) {
  const comments = use(commentsPromise);

  return (
    <ul>
      {comments.map((c) => <li key={c.id}>{c.text}</li>)}
    </ul>
  );
}

function Page({ commentsPromise }) {
  return (
    <Suspense fallback={<p>Loading...</p>}>
      <Comments commentsPromise={commentsPromise} />
    </Suspense>
  );
}
```

> `use` is the only "hook" that may be called **conditionally** — inside an `if`, a loop, or after an early return. It is not bound by the Rules of Hooks in 7.2.

---

### The three timing hooks, side by side

These are the three easiest to confuse. The distinction is **when** they fire relative to the browser painting the screen.

| Hook | Fires | Blocks paint? | Use it for |
|---|---|---|---|
| `useInsertionEffect` | **Before** DOM mutations are read | Yes | Injecting `<style>` tags (CSS-in-JS libraries only) |
| `useLayoutEffect` | **After** DOM mutations, **before** paint | Yes | Measuring or mutating layout so the user never sees a flash |
| `useEffect` | **After** paint | No | Everything else — data fetching, subscriptions, logging |

**Default to `useEffect`.** Only move up this table when you have a specific visual-flash or style-injection problem.

---

---

# PART 8 — Handling Events

## 8.1 How events work in React

In React, event handling is similar to handling events in traditional JavaScript, but with some **syntactical differences**.

React uses a **synthetic event system** that normalizes the differences between browser implementations and provides a **consistent way to handle events across different browsers**.

```
App  ⇄  React Virtual DOM  ⇄  DOM
     builds/modifies  →
     ←  delivers events
```

### The three differences from plain HTML

1. **React events are named in camelCase** instead of lowercase.
   - HTML: `onclick`, `onchange`
   - React: `onClick`, `onChange`
2. **A function is passed as the event handler instead of a string.**
   - HTML: `<button onclick="showMessage()">Hello</button>`
   - React: `<button onClick={showMessage}>Hello</button>`
3. **You cannot return `false` to prevent default behaviour.** You must call `preventDefault` explicitly.

---

## 8.2 Handling a click

```jsx
import React from 'react';

function Button() {
  const handleClick = () => {
    console.log('Button clicked');
  };

  return <button onClick={handleClick}>Click me</button>;
}

export default Button;
```

When the button is clicked, the `handleClick` function is called and the message is logged.

React provides a set of predefined event handlers: `onClick`, `onChange`, `onSubmit`, and more.

---

## 8.3 Passing arguments to an event handler

To pass an argument, wrap the handler in an **arrow function**:

```jsx
function Football() {
  const shoot = (a) => {
    alert(a);
  };

  return (
    <button onClick={() => shoot("Goal")}>Take shot!</button>
  );
}
```
Clicking "Take shot!" pops an alert saying `Goal`.

The general form: `<button onClick={() => handleClick(parameter)}>`

---

## 8.4 Binding event handlers

### In class components
In class components, we bind event handlers in the constructor or use class-fields syntax. **Binding ensures that the `this` keyword within the event handler refers to the component instance.**

```jsx
import React from 'react';

class Counter extends React.Component {
  constructor(props) {
    super(props);
    this.state = { count: 0 };
    this.incrementCount = this.incrementCount.bind(this);   // ← the bind
  }

  incrementCount() {
    this.setState({ count: this.state.count + 1 });
  }

  render() {
    return (
      <div>
        <p>Count: {this.state.count}</p>
        <button onClick={this.incrementCount}>Increment</button>
      </div>
    );
  }
}

export default Counter;
```

### The arrow function alternative
The arrow function is an ES6 feature. **If you use arrow functions, it is not necessary to bind the event to `this`.**

```jsx
import React, { Component } from 'react';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = { data: 'www.javatpoint.com' };
  }

  handleEvent = () => {          // ← arrow function class field; no bind needed
    console.log(this.props);
  }

  render() {
    return (
      <div className="App">
        <h2>React Constructor</h2>
        <input type="text" value={this.state.data} />
        <button onClick={this.handleEvent}>Please Click</button>
      </div>
    );
  }
}

export default App;
```

### In functional components — `useCallback`
In functional components, we can use the `useCallback` hook to bind event handlers. `useCallback` **memoizes** the event handler function, ensuring it doesn't change on each re-render unless its dependencies change.

```jsx
import React, { useState, useCallback } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  const incrementCount = useCallback(() => {
    setCount(count + 1);
  }, [count]);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={incrementCount}>Increment</button>
    </div>
  );
}

export default Counter;
```

---

## 8.5 The event object and synthetic events

Event handlers are provided with a **synthetic event object** that wraps the underlying browser event. This synthetic event object provides a **consistent interface** for accessing event-related data and methods across different browsers.

For example, to access the value of an input field when it changes, use `event.target.value`:

```jsx
import React, { useState } from 'react';

function InputField() {
  const [value, setValue] = useState('');

  const handleChange = (event) => {
    setValue(event.target.value);
  };

  return (
    <div>
      <input type="text" value={value} onChange={handleChange} />
      <p>Value: {value}</p>
    </div>
  );
}

export default InputField;
```

The event object is automatically passed to the handler. By accessing `event.target.value` we get the current value of the input and update the component's state.

### A full class-based example
```jsx
import React, { Component } from 'react';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = { companyName: "" };
  }

  changeText(event) {
    this.setState({ companyName: event.target.value });
  }

  render() {
    return (
      <div>
        <h2>Simple Event</h2>
        <label htmlFor="companyName">Enter Company Name</label>
        <input
          type="text"
          id="companyName"
          onChange={this.changeText.bind(this)}
        />
        <h4>You entered: {this.state.companyName}</h4>
      </div>
    );
  }
}

export default App;
```

---

## 8.6 Event delegation

**Event delegation is a technique that allows us to handle events on multiple elements using a single event handler attached to a common parent element.**

Instead of attaching event handlers to each individual child, the parent element handles the events and determines which child element triggered the event.

**This approach can improve performance and reduce the number of event handlers needed.**

---
---

# PART 9 — Conditional Rendering, Lists and Keys

## 9.1 Conditional rendering

Your components will often need to display different things depending on different conditions. In React, you can conditionally render JSX using ordinary JavaScript syntax.

### Method 1 — `if` statement
The easiest way, used in the render method before the return.

```jsx
function UserLogin(props) {
  return <h1>Welcome Back</h1>;
}

function GuestLogin(props) {
  return <h1>Please Sign Up</h1>;
}

function SignUp(props) {
  const isLoggedIn = props.isLoggedIn;
  if (isLoggedIn) {
    return <UserLogin />;
  }
  return <GuestLogin />;
}

ReactDOM.render(
  <SignUp isLoggedIn={false} />,
  document.getElementById('root')
);
```

### Method 2 — Logical `&&` operator
Renders the right-hand side only if the left-hand side is truthy.

```jsx
function Garage(props) {
  const cars = props.cars;
  return (
    <>
      <h1>Garage</h1>
      {cars.length > 0 &&
        <h2>
          You have {cars.length} cars in your garage.
        </h2>
      }
    </>
  );
}

const cars = ['Ford', 'BMW', 'Audi'];
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Garage cars={cars} />);
```
Output:
```
Garage
You have 3 cars in your garage
```

### Method 3 — Ternary operator
`condition ? ifTrue : ifFalse`

```jsx
function Goal(props) {
  const isGoal = props.isGoal;
  return (
    <>
      {isGoal ? <MadeGoal /> : <MissedGoal />}
    </>
  );
}

root.render(<Goal isGoal={false} />);
```
Output: `MISSED`

```jsx
render() {
  const isLoggedIn = this.state.isLoggedIn;
  return (
    <div>
      Welcome {isLoggedIn ? 'Back' : 'Please login'}
    </div>
  );
}
```

> **Best practice:** avoid nested ternaries — extract to a variable or a component instead.

### Method 4 — Switch case
```jsx
function NotificationMsg({ text }) {
  switch (text) {
    case 'Hi all':
      return <Message text={text} />;
    case 'Hello JavaTpoint':
      return <Message text={text} />;
    default:
      return null;
  }
}
```

### Method 5 — Conditional rendering with enums
An enum is a great way to have multiple conditional renders. It is **more readable** than a switch-case.

```jsx
function NotificationMsg({ text, state }) {
  return (
    <div>
      {{
        info: <Message text={text} />,
        warning: <Message text={text} />,
      }[state]}
    </div>
  );
}
```

### Early return
If you don't want a component to render at all, return `null` — or return some JSX. This is called an **early return**.

```jsx
if (!allRestaurants) return null;

if (filteredRestaurants?.length === 0) return <h1>No matches</h1>;
```

---

## 9.2 Lists

Lists are used to display data in an ordered format, and are mainly used to display menus on websites. The **`map()`** function is used to traverse the list.

```jsx
var numbers = [1, 2, 3, 4, 5];
const multiplyNums = numbers.map((number) => {
  return (number * 5);
});
console.log(multiplyNums);
```
Output: `[5, 10, 15, 20, 25]`

**Rendering a list of elements:**
```jsx
import React from 'react';
import ReactDOM from 'react-dom';

const myList = ['Peter', 'Sachin', 'Kelvin', 'Dhoni', 'Alisa'];
const listItems = myList.map((item) => {
  return <li>{item}</li>;
});

ReactDOM.render(
  <ul>{listItems}</ul>,
  document.getElementById('app')
);
```

**As a component receiving props:**
```jsx
import React from 'react';
import ReactDOM from 'react-dom';

function NameList(props) {
  const listItems = props.myList.map((item) =>
    <li>{item}</li>
  );
  return (
    <div>
      <h2>React Map example</h2>
      <ul>{listItems}</ul>
    </div>
  );
}

const myLists = ['A', 'B', 'C', 'D'];

ReactDOM.render(
  <NameList myList={myLists} />,
  document.getElementById('app')
);
```

> **In functional programming we don't use `for` loops — we use `.map`.** `.map` is the best way to render a list.

---

## 9.3 Keys — and why they matter enormously

**A key is a unique identifier.** In React, it is used to identify **which items have changed, been updated, or been deleted** from a list.

It is useful when you dynamically create components, or when the user alters the list. It also helps determine which component in a collection needs to be rendered, instead of re-rendering the entire set of components every time.

```jsx
const stringList = ['Peter', 'Sachin', 'Kelvin', 'Dhoni', 'Alisa'];
const updatedLists = stringList.map((strList) => (
  <li key={strList.id}>{strList}</li>
));
```

If there are no stable IDs for the rendered items, you *can* assign the item index as the key:
```jsx
const updatedLists = stringList.map((strList, index) => (
  <li key={index}>{strList}</li>
));
```

> ⚠️ But be careful — see the warning about index keys below.

### The problem keys solve

Whenever React updates the DOM, consider this list:
```html
<ul>
  <li>Duke</li>
  <li>Villanova</li>
</ul>
```

If we add an element at the **end**, the tree diffing works well. But if we introduce a new child at the **top**:
```html
<ul>
  <li>Connecticut</li>   <!-- new, inserted first -->
  <li>Duke</li>
  <li>Villanova</li>
</ul>
```
React has to do a lot of work — **React will have to re-render everything and change the whole DOM tree**. In a large-scale application, this is far too expensive.

**The solution: keys.**
```html
<ul>
  <li key="2014">Connecticut</li>
  <li key="2015">Duke</li>
  <li key="2016">Villanova</li>
</ul>
```
When children have keys, React uses the key to **match children in the original tree with children in the subsequent tree**, making tree conversion efficient. React now has to do very little work.

> **Always use keys whenever you have multiple children.**

If you forget, React will warn you in the console:
> *"Each child in a list should have a unique 'key' prop."*

### The impact of using indexes as keys
Using indexes as keys can have a **negative impact on performance** because they don't provide a **stable identity** for elements, and React has to rely on the order of elements in the array to determine which elements have changed. This can lead to unnecessary re-renders.

> **Best practice:** never use the array index as a key if the list can reorder, have items inserted, or have items deleted.

---
---

# PART 10 — Forms

## 10.1 Why forms matter

Forms are an integral part of any modern web application. They allow users to interact with the application as well as gather information from the user. Forms perform many tasks that depend on the nature of your business requirements and logic, such as authenticating the user.

React offers a **stateful, reactive approach** to building a form. The **components**, rather than the DOM, usually handle the React form.

There are two kinds:
1. **Uncontrolled components**
2. **Controlled components**

---

## 10.2 Uncontrolled components

The uncontrolled component input is similar to a traditional HTML form input. **The DOM itself handles the form data.** HTML elements maintain their own state, which is updated when the input value changes.

```jsx
import React, { Component } from 'react';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.updateSubmit = this.updateSubmit.bind(this);
    this.input = React.createRef();
  }

  updateSubmit(event) {
    alert("You have entered the username and company name successfully");
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.updateSubmit}>
        <h1>Uncontrolled Form</h1>
        <label>
          Name:
          <input type="text" ref={this.input} />
        </label>
        <label>
          Company Name:
          <input type="text" ref={this.input} />
        </label>
        <input type="submit" value="Submit" />
      </form>
    );
  }
}

export default App;
```

Simple form:
```jsx
<input ref={inputRef} defaultValue="Hi" />
```
> **Best practice:** read via ref on submit; good for simple or performance-sensitive forms.

---

## 10.3 Controlled components

**Controlled components are components where the state of the form inputs is controlled by React.** This means the value of the input elements is stored in the component's state, and any changes to the input values are handled through React state updates.

Controlled components have a function that governs the data passing into them **on every `onChange` event**, rather than grabbing the data only once.

Controlled components allow us to have more control over the form inputs and enable features like **validation and data manipulation**.

### The three steps to build a controlled component

1. **Initialize the state** — Create state variables in the component to store the values of the form inputs. Use the `useState` hook.
2. **Connect the input to the state** — Bind the `value` of the input element to the corresponding state variable. This ensures the input displays the current value and that any changes are reflected in the state.
3. **Handle input changes** — Attach an event handler to the input's `onChange` event. In the handler, update the state variable with the new value entered by the user.

### Functional version (modern)
```jsx
import React, { useState } from 'react';

function Form() {
  const [name, setName] = useState('');

  const handleInputChange = (event) => {
    setName(event.target.value);
  };

  return (
    <form>
      <label>
        Name:
        <input type="text" value={name} onChange={handleInputChange} />
      </label>
      <button type="submit">Submit</button>
    </form>
  );
}

export default Form;
```

### Class version (legacy)
```jsx
import React, { Component } from 'react';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = { value: "" };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({ value: event.target.value });
  }

  handleSubmit(event) {
    alert("You have submitted the input successfully: " + this.state.value);
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <h1>Controlled Form</h1>
        <label>
          Name:
          <input
            type="text"
            value={this.state.value}
            onChange={this.handleChange}
          />
        </label>
        <input type="submit" value="Submit" />
      </form>
    );
  }
}

export default App;
```

> **Best practice:** React state is the **single source of truth**.

---

## 10.4 Controlled vs Uncontrolled — the comparison

| Controlled | Uncontrolled |
|---|---|
| It accepts the current value as a **prop** | It uses a **ref** for its current values |
| Better control over form elements and data | Limited control over form elements |
| Does **not** maintain internal state | **Maintains** internal state |
| Data is controlled by the **parent component** | Data is controlled by the **DOM** |
| **Allows** validation control | Does **not** allow validation control |

> ⚠️ **Common mistake:** a "bad controlled/uncontrolled" input.
>
> | ❌ DON'T | ✅ DO |
> |---|---|
> | `<input value={v} />` — no `onChange` | `<input value={v} onChange={onChange} />` |

---

## 10.5 Handling form submission and validation

To handle form submission, attach an event handler to the form element's **`onSubmit`** event. In the handler, perform any necessary **validation and data processing** before taking appropriate actions, such as making API calls or updating the component's state.

```jsx
import React, { useState } from 'react';

function Form() {
  const [name, setName] = useState('');

  const handleInputChange = (event) => {
    setName(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    // Perform form validation and data processing
    if (name.trim() === '') {
      alert('Please enter a name');
      return;
    }

    // submit the form or take other actions
    console.log('Form submitted:', name);
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Name:
        <input type="text" value={name} onChange={handleInputChange} />
      </label>
      <button type="submit">Submit</button>
    </form>
  );
}

export default Form;
```

The `handleSubmit` handler prevents the default form submission behaviour using **`event.preventDefault()`**. Then we perform validation, such as checking if the name field is empty. If validation fails, display an error message. If it passes, proceed with submitting.

---

## 10.6 A note on form libraries

Be conscious about what packages you use. You should use big packages when you have complex things to do.

For example: if you have to build a lot of big, lengthy forms where each input box has its own RegEx check, pattern check, and validation — instead of building all the components yourself, use a package like **Formik** (an open-source library). You can also use **React Hook Form** instead of Formik.

---
---

# PART 11 — Styling in React

## 11.1 The approaches

Styling in React refers to the process of applying visual styles to the components and elements of a React application.

There are several approaches:
1. **Inline styles**
2. **CSS stylesheets**
3. **CSS modules**
4. **Styling libraries** — styled-components, CSS-in-JS
5. **Utility frameworks** — Tailwind CSS, Bootstrap, Material UI

---

## 11.2 Inline styling

To style an element with the inline `style` attribute, **the value must be a JavaScript object**.

```jsx
const Header = () => {
  return (
    <>
      <h1 style={{color: "red"}}>Hello Topper</h1>
      <p>Welcome to Topperworld!</p>
    </>
  );
};
```

> **Why two sets of curly braces?** In JSX, JavaScript expressions are written inside curly braces — and since JavaScript objects also use curly braces, the styling above is written inside **two** sets of curly braces. The outer pair says "here comes JavaScript", the inner pair is the object literal.

### camelCase property names
Use `backgroundColor` instead of `background-color`:
```jsx
const Header = () => {
  return (
    <>
      <h1 style={{backgroundColor: "lightblue"}}>Hello</h1>
      <p>Add style</p>
    </>
  );
};
```

### Using a separate style object
```jsx
const Header = () => {
  const myStyle = {
    color: "white",
    fontFamily: "sans-serif",
    backgroundColor: "red"
  };

  return (
    <>
      <h1 style={myStyle}>Hello</h1>
      <p>Welcome to React</p>
    </>
  );
};
```

Or defined outside the component:
```jsx
const styleObj = {
  backgroundColor: "red",
};

const jsx = (
  <div style={styleObj}>
    <h1>Hello</h1>
    <h2>World</h2>
  </div>
);
```

Inline styles offer a straightforward way to apply styles directly to components, **but they can become cumbersome for complex styling requirements**.

---

## 11.3 CSS stylesheets

Write your CSS in a separate `.css` file and import it into your application.

**App.css**
```css
body {
  background-color: #282c34;
  color: white;
  font-family: sans-serif;
  padding: 40px;
  text-align: center;
}
```

**App.js**
```jsx
import React from 'react';
import './App.css';

class App extends React.Component {
  render() {
    return (
      <div>
        <h1>Hello JavaTpoint</h1>
        <p>You can find all CS tutorials here</p>
      </div>
    );
  }
}

export default App;
```

Then give a `className` to your elements:
```jsx
const jsx = (
  <div className="jsx">
    <h1>Hello</h1>
    <h2>World</h2>
  </div>
);
```
```css
.jsx {
  background-color: blue;
}
```

---

## 11.4 CSS modules

**CSS modules are a popular approach for styling React components.** With CSS modules, you write CSS stylesheets that are **scoped to individual components**, preventing style conflicts across different components.

All class names and animation names are scoped locally by default. Styles are available only for the component that imports them — meaning any styling you add can never be applied to other components without your permission, and you never need to worry about name conflicts.

Create a CSS module with the **`.module.css`** extension:

**MyComponent.module.css**
```css
.container {
  color: red;
  font-size: 16px;
  font-weight: bold;
}
```

**MyComponent.js**
```jsx
import styles from './MyComponent.module.css';

function MyComponent() {
  return <div className={styles.container}>Hello, world!</div>;
}
```

Another example:

**myStyles.module.css**
```css
.mystyle {
  background-color: #cdc0b0;
  color: Red;
  padding: 10px;
  font-family: Arial;
  text-align: center;
}

.parastyle {
  color: Green;
  font-family: Arial;
  font-size: 35px;
  text-align: center;
}
```

```jsx
import React from 'react';
import styles from './myStyles.module.css';

class App extends React.Component {
  render() {
    return (
      <div>
        <h1 className={styles.mystyle}>Hello JavaTpoint</h1>
        <p className={styles.parastyle}>It provides great CS tutorials</p>
      </div>
    );
  }
}

export default App;
```

**CSS modules provide encapsulated styling and allow for better organisation and reuse of styles.**

---

## 11.5 Styled components (CSS-in-JS)

**styled-components** is a popular library that enables writing CSS styles **directly within the JavaScript code**. It allows us to define styles as components, where the styles are automatically applied to the corresponding elements.

```jsx
import styled from 'styled-components';

const StyledDiv = styled.div`
  color: red;
  font-size: 16px;
  font-weight: bold;
`;

function MyComponent() {
  return <StyledDiv>Hello, world!</StyledDiv>;
}
```

The `StyledDiv` component is created using the `styled` function. The styles are defined using **template literal syntax**, which allows us to write CSS directly in the component.

**What styled-components provides:**
- Automatic critical CSS
- No class name bugs
- Easier deletion of CSS
- Simple dynamic styling
- Painless maintenance

### Other CSS-in-JS libraries
Apart from styled-components, there are other CSS-in-JS libraries in the React ecosystem, such as **Emotion, Glamorous, and Aphrodite**. These offer similar functionality.

CSS-in-JS libraries provide a range of features, including **dynamic styles, theme support, and style composition**. They offer a more flexible and powerful approach to styling, especially for complex applications.

---

## 11.6 Dynamic class names

Conditionally apply a CSS class based on state, using a template literal:
```jsx
<div className={`box ${isActive ? "active" : ""}`}></div>
```

---

> **Overall:** styling in React can be achieved using various approaches. **The choice depends on the specific needs of your project, the complexity of the styling requirements and personal preference.**

---
---

# PART 12 — React and APIs

## 12.1 Making API requests

In React, interacting with **APIs** (Application Programming Interfaces) is a common task when we need to fetch data from external sources such as databases, servers, or third-party services. This data can be used to dynamically update the user interface, display content, or perform other operations.

To make API requests in React, we can use JavaScript's built-in **`fetch()`** function or a third-party library like **Axios**.

- The **`fetch()`** function is a modern, native browser feature for making network requests.
- **Axios** is a widely used third-party library known for its simplicity and flexibility.

### Using `fetch()` with `.then()`
```jsx
import React, { useEffect, useState } from 'react';

function MyComponent() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('https://api.example.com/data')
      .then((response) => response.json())
      .then((data) => setData(data))
      .catch((error) => console.error('Error fetching data:', error));
  }, []);

  return <div>{data ? JSON.stringify(data) : 'Loading ...'}</div>;
}
```

The `fetch()` function is used within the `useEffect()` hook to make the API request. The response is converted to JSON format using `response.json()`, and the data is stored in the `data` state variable using `setData()`.

---

## 12.2 Asynchronous operations — `async/await`

API requests are **asynchronous** operations because they take some time to complete and the result is not immediately available. In React, we can use **`async/await`** or **`.then()`** syntax.

```jsx
import React, { useEffect, useState } from 'react';

function MyComponent() {
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('https://api.example.com/data');
        const data = await response.json();
        setData(data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      {data ? JSON.stringify(data) : 'Loading...'}
    </div>
  );
}
```

The `fetchData` function is defined as an **asynchronous function**, allowing the use of `await` within it to wait for the API's response. The `await` keyword is used before the `fetch()` and `response.json()` calls, which makes the function wait until the respective promises are resolved.

> ⚠️ **Common mistake:** don't make the `useEffect` callback itself `async`.
>
> | ❌ DON'T | ✅ DO |
> |---|---|
> | `useEffect(async () => {...}, [])` | `useEffect(() => { (async()=>{...})(); }, [])` |

---

## 12.3 Where should you call the API?

This is a design decision that matters. Consider two possible sequences:

**Case 1 — fetch first, then render**
```
User loads the website → Make an API call (300ms) → Render page (200ms)   = 500ms
```
The user stares at a blank screen for 300ms.

**Case 2 — render first, then fetch, then update**
```
User loads the website → Render the initial page (100ms) → call the API (300ms) → update the UI (100ms)   = 500ms
```

**Case 2 is the better way.** The total time is the same, but the user sees something immediately. To make this happen, React gives us the **`useEffect`** hook with an empty dependency array.

```jsx
useEffect(() => {
  getRestaurants();
}, []);

async function getRestaurants() {
  const data = await fetch("https://some-api-url");
  const json = await data.json();
  console.log(json);
  setRestaurants(json?.data?.cards[2]?.data?.data?.cards);
}
```

> **Where NOT to call the API:** don't call `fetch` directly in the component body. On every state change or UI update it would run again — an infinite loop.

---

## 12.4 CORS

**CORS (Cross Origin Resource Sharing)** is an HTTP-header based mechanism that allows a server to indicate any cross origins (domain, scheme or port) other than its own, from which a browser should permit loading resources.

There are security parameters that mean a browser will **block** you from calling a third-party API from your localhost. To work around this during development, there is a Chrome plugin: **Allow CORS: Access-Control-Allow-Origin**. Adding this plugin lets you bypass the CORS error while developing.

### The `crossorigin` attribute
The `crossorigin` attribute provides support for CORS. If we serve React from a CDN, keep the `crossorigin` attribute set:
```html
<script crossorigin src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
```
This indicates that the script should be loaded from a different origin.

---

## 12.5 Handling the response

Once the API response is obtained, we can handle the data appropriately. The fetched data is stored in the `data` state variable. We can use this data to **update the UI, perform calculations, or pass it down to other components as props**.

In the examples above, a simple representation of the fetched data is displayed using `JSON.stringify()`, but in a real-world scenario you would render the data in a more structured and meaningful way based on your application's requirements.

> **Remember to handle errors gracefully**, using `try/catch` blocks or `.catch()` methods to prevent the application from breaking if the API request fails.

By using the appropriate API request methods and handling asynchronous operations effectively, React can efficiently interact with APIs and update the UI based on the received data.

---

## 12.6 Shimmer UI — what to show while loading

This is an important UX concept.

When data hasn't arrived yet, old data renders first for a few seconds and then new data comes. If we remove the old data, the page shows an ugly empty UI. So the initial screen should be a **loader / Shimmer UI** — a basic skeleton.

> **The research behind it:** people used to see spinning loaders first, and then suddenly all the content would appear. **This is a bad user experience.** According to psychology, the human brain doesn't like to see so many fluctuations in the UI. Psychologists figured out that instead of spinners, **empty boxes shaped like the real content** should be shown. It is a much better UI experience for users because sudden changes are not happening — your eyes don't hurt. This is known as **Shimmer UI**.

**Shimmer UI resembles the actual UI, so users understand how quickly the app will load even before the content has shown up. Every big company follows this.**

### A Shimmer component
```jsx
const Shimmer = () => {
  return (
    <div className="restaurant-list">
      {Array(10).fill("").map((e, index) => (
        <div className="shimmer-card" key={index}></div>
      ))}
    </div>
  );
};

export default Shimmer;
```

### Wiring it up with conditional rendering
Pseudocode:
1. if `restaurants` is empty ⇒ load Shimmer UI
2. if `restaurants` has data ⇒ load the actual UI

```jsx
return (restaurants.length === 0) ? <Shimmer /> : (
  <>
    {/* the real UI */}
  </>
);
```

---
---

# PART 13 — React Router

## 13.1 What is routing?

**Routing is the process in which a user is directed to different pages based on their action or request.**

React Router is used to define multiple routes in the application. It is a standard library built on top of React and used to create routing in a React application. It provides synchronous URL updates in the browser with the data that will be displayed on the web page.

React Router is mainly used for developing **Single Page Applications**.

### The three routing packages
1. **`react-router`** — provides the core routing components and functions.
2. **`react-router-native`** — used for mobile applications.
3. **`react-router-dom`** — used for **web application design**. This is the one you want.

### Installation
```bash
npm install react-router-dom --save
```
or
```bash
npm i -D react-router-dom
```

---

## 13.2 Single Page Applications (SPA)

**React apps are SPAs.**

- Having SPAs means the page will **not reload**; it will not make a network call when we change pages.
- An SPA loads a **single HTML page** and dynamically updates the page in response to user interaction without reloading the entire page.
- This approach allows for **faster navigation** and a more seamless user experience.

### The problem with the plain anchor tag
An `<a>` tag will **reload the entire page** when clicked. It disrupts the user experience and can result in a slower page load time. **This causes problems for Single-Page Applications.**

### Two types of routing

**Server-side routing**
- All our pages come from the server.
- Every navigation makes a network call, gets the HTML/JS/CSS and loads the whole page.

**Client-side routing**
- Dynamically updates the content of the SPA in response to a change in the URL.
- Does **not** do a full page reload.

React Router gives us the **`<Link>`** component for client-side routing.

---

## 13.3 Setting up routes — the modern approach

Import `createBrowserRouter` — a function from `react-router-dom` that helps us create routing. `createBrowserRouter` is the **recommended router for all React Router web projects**.

```jsx
import { createBrowserRouter, RouterProvider } from "react-router-dom";

const appRouter = createBrowserRouter([
  {
    path: "/",
    element: <AppLayout />,
  },
  {
    path: "/about",
    element: <About />,
  },
]);

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<RouterProvider router={appRouter} />);
```

Here we define where our app will get loaded for each path. This is where we create the **routing configuration**.

Providing the config alone isn't enough — we need to hand `appRouter` to our app using the **`RouterProvider`** component, which also comes from `react-router-dom`.

---

## 13.4 Setting up routes — the classic `<Route>` approach

```jsx
import React from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import Home from './components/Home';
import About from './components/About';
import Contact from './components/Contact';

function App() {
  return (
    <Router>
      <Route exact path="/" component={Home} />
      <Route exact path="/about" component={About} />
      <Route path="/contact" component={Contact} />
    </Router>
  );
}

export default App;
```

- Each `<Route>` component represents a different route and specifies the component to render when that route is accessed.
- The **`exact`** keyword ensures the route matches **exactly** the specified path.
- The **`path`** prop defines the URL path.
- The **`component`** prop specifies the component to render.

### Other core components
- **`<BrowserRouter>`** — used for handling URLs
- **`<HashRouter>`** — used to handle static requests

### Another routes-based syntax
```jsx
export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="blogs" element={<Blogs />} />
          <Route path="contact" element={<Contact />} />
          <Route path="*" element={<NoPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}
```

---

## 13.5 Navigation with `<Link>`

To enable navigation between routes, use the **`<Link>`** component. The `<Link>` component renders an anchor tag (`<a>`) with the specified destination path — but **without** the full page reload.

```jsx
import React from 'react';
import { Link } from 'react-router-dom';

function Navigation() {
  return (
    <nav>
      <ul>
        <li><Link to="/">Home</Link></li>
        <li><Link to="/about">About</Link></li>
        <li><Link to="/contact">Contacts</Link></li>
      </ul>
    </nav>
  );
}

export default Navigation;
```

The **`to`** prop specifies the destination path to navigate to when the link is clicked.

---

## 13.6 Error pages

`react-router-dom` gives us a better UI for error pages. Create your own `Error.js` and pass it to the router config as **`errorElement`**:

```jsx
{
  path: "/",
  element: <AppLayout />,
  errorElement: <Error />,
}
```

If there is an error in the path, it will load the error element.

To show more information about the error, `react-router-dom` gives us the **`useRouteError`** hook. It catches all routing errors so we can show them to the user, and prevents red errors flooding the console.

```jsx
import { useRouteError } from "react-router-dom";

const Error = () => {
  const err = useRouteError();

  return (
    <div>
      <h1>Oops! Something went wrong</h1>
      <h2>
        {err.status + " : " + err.statusText}
      </h2>
    </div>
  );
};

export default Error;
```

---

## 13.7 Nested routes and `<Outlet>`

To keep the Header and Footer on every page, make the other pages **children** of `<AppLayout />`:

```jsx
const appRouter = createBrowserRouter([
  {
    path: "/",
    element: <AppLayout />,
    errorElement: <Error />,
    children: [
      {
        path: "/about",
        element: <About />,
      },
      {
        path: "/contact",
        element: <Contact />,
      },
    ]
  },
]);
```

Then in the layout, use **`<Outlet />`**:

```jsx
import { Outlet } from "react-router-dom";

const AppLayout = () => {
  return (
    <>
      <Header />
      <Outlet />      {/* children get rendered here, according to the route */}
      <Footer />
    </>
  );
};
```

**All the children will go inside `<Outlet />`, according to the route.**

### Nested routes, classic syntax
```jsx
import { BrowserRouter as Router, Route } from 'react-router-dom';
import User from './components/User';
import UserProfile from './components/UserProfile';

function App() {
  return (
    <Router>
      <Route path="/user/:id" component={User} />
      <Route path="/user/:id/profile" component={UserProfile} />
    </Router>
  );
}
```
When a URL matches the nested route, **both** the `User` and `UserProfile` components will be rendered. This allows us to create complex route hierarchies and nested views.

---

## 13.8 Dynamic routing and route parameters

**Dynamic routing is the process of rendering components in response to a change in the application's URL.**

Route parameters are specified by adding a **colon (`:`)** followed by the parameter name in the `path`:

```jsx
{
  path: "/restaurant/:id",     // :id is dynamic — it can be anything
  element: <RestaurantMenu />
}
```

To read the parameter passed in the URL, `react-router-dom` gives us the **`useParams`** hook:

```jsx
import { useParams } from "react-router-dom";

const RestaurantMenu = () => {
  const params = useParams();
  const { id } = params;

  return (
    <div>
      <h1>Restaurant id: {id}</h1>
    </div>
  );
};

export default RestaurantMenu;
```

### A full dynamic page with an API call
```jsx
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import Shimmer from "./Shimmer";

const RestaurantMenu = () => {
  const { resId } = useParams();
  const [restaurant, setRestaurant] = useState(null);

  useEffect(() => {
    getRestaurantInfo();
  }, []);

  async function getRestaurantInfo() {
    const data = await fetch("https://api-url?id=" + resId);
    const json = await data.json();
    setRestaurant(json.data);
  }

  return !restaurant ? (
    <Shimmer />
  ) : (
    <div>
      <h1>Restaurant id: {resId}</h1>
      <h2>{restaurant.name}</h2>
      <h3>{restaurant.area}</h3>
      <h3>{restaurant.city}</h3>
      <h3>{restaurant.avgRating}</h3>

      <h1>Menu</h1>
      <ul>
        {Object.values(restaurant?.menu?.items).map((item) => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default RestaurantMenu;
```

---

## 13.9 Benefits of React Router

1. It is **not necessary to set the browser history manually**.
2. `<Link>` is used to navigate internal links in the application — it is similar to an anchor tag but without the reload.
3. It uses a **Switch** feature for rendering.
4. The router needs only a single child element.

---
---

# PART 14 — How React Works Inside

## 14.1 The Virtual DOM

**A virtual DOM object is a representation of the original DOM object.** It is a lightweight, in-memory representation of the actual DOM.

**Why it exists:** it is used to improve the performance of updates and changes to the actual DOM **by reducing the number of expensive DOM manipulations**.

Whenever any modification happens in the web application, the entire UI is re-rendered in the virtual DOM representation. React then compares the new virtual DOM to the previous one, and **the real DOM updates only the things that have actually changed**.

### How it works step by step
1. A component's state or props change.
2. React creates a **new virtual DOM tree**.
3. React **compares** it to the previous tree (the diff).
4. React applies **only the minimal set of changes** necessary to the actual DOM.

```
Virtual DOM:   State Change  →  Compute Diff  →  Re-render
Browser DOM:   (unchanged)      (unchanged)      only the changed node updates
```

### Keeping a representation of the DOM
Let your DOM look like this:
```
                ROOT
        /        |        \
      HEAD     BODY      FOOTER
             /   |   \
          REST1 REST2  REST3
          /  \
        img   h2
```
React keeps a copy of this tree in memory — that copy is the **Virtual DOM**.

---

## 14.2 Real DOM vs Virtual DOM vs Shadow DOM

| Term | What it is |
|---|---|
| **Real DOM** | The actual tree-like structure of a web page, which can be manipulated directly to change the layout or content. Slow to manipulate. |
| **Virtual DOM** | A lightweight in-memory representation of the actual DOM, used by React to optimize the performance of UI updates. |
| **Shadow DOM** | A feature of **web browsers** (not React) that allows developers to create a separate DOM tree, called a shadow tree, that is attached to a specific element and is hidden from the main document. It allows scoping of CSS and JavaScript within a specific element. |

> **The key distinction:** Virtual DOM is a React concept for performance. Shadow DOM is a browser feature for encapsulation. They are unrelated despite the similar names.

---

## 14.3 Reconciliation

**Reconciliation is the process that React uses to determine the minimal set of changes to be made to the actual DOM.**

- Reconciliation is an **algorithm** that React uses to **diff** one tree from another.
- It uses a **Diff Algorithm** to determine what needs to change and what does not in the UI — finding the difference between one tree (the Actual DOM) and the other (the Virtual DOM).
- The Diff Algorithm then finds out what needs to be updated and changes **only that small portion**.

It helps make React applications fast and efficient by minimizing the amount of work needed to update changes. **You don't have to worry about what changes on every update.**

```
Reconciliation:
   Virtual DOM  --Diff-->  New Virtual DOM  --Update-->  Browser DOM
```

- The `render()` function creates a tree of React elements.
- On the next state or props update, `render()` will return a different tree of React elements.
- React diffs the two.

React diffs the new element tree against the previous one **by type and key**, updating only the DOM nodes that actually changed.

---

## 14.4 React Fiber

**React Fiber is a new reconciliation algorithm that was introduced in React 16.**

- It's a **reconciliation engine**, responsible for the diff algorithm.
- It is designed to improve the **performance and flexibility** of React by **breaking down the render process into smaller, asynchronous chunks**.

**The main goal of React Fiber** is to improve the performance and responsiveness of web applications by breaking down the render process into smaller, asynchronous chunks. This allows React to more effectively utilize the main thread and to better handle complex user interfaces.

---

## 14.5 The two render phases

React does rendering in **two phases**:

### 1. The Render Phase
- This phase is **fast**.
- It includes the **constructor** and **render** methods.
- React completes the render phase of every child before moving on.

### 2. The Commit Phase
- The phase where **React modifies the actual DOM**.
- `componentDidMount` is called after the initial render has finished.
- The commit phase is **slow** (relative to render).

### Why this matters — a demonstration

Suppose `<About />` (parent) renders two `<Profile />` children. The order of execution is:

1. Parent — constructor
2. Parent — render
3. First child — constructor
4. First child — render
5. Second child — constructor
6. Second child — render
   ← **COMMIT PHASE STARTS**
7. First child — componentDidMount
8. Second child — componentDidMount
9. Parent — componentDidMount

**Explanation:** React completes the **render phase of every child** and only *after that* moves to the commit phase. If after the first child's render React immediately called that child's `componentDidMount` (which might make an API call), the second child would be left waiting. So React **batches** the render phases together.

### Lifecycle diagram

| Phase | Render Phase | Commit Phase |
|---|---|---|
| **MOUNTING** | constructor → render | React updates DOM and refs → `componentDidMount` |
| **UPDATING** (new props / `setState()` / `forceUpdate()`) | render | React updates DOM and refs → `componentDidUpdate` |
| **UNMOUNTING** | — | `componentWillUnmount` |

---

## 14.6 Why is React fast? — the summary

- It has the **Virtual DOM**, **Reconciliation** and the **Diff algorithm**.
- In the diff algorithm, the current tree is compared with the new tree and only the difference is reflected on the DOM.
- **React Fiber** is the updated reconciliation algorithm.
- React is fast because of its fast DOM manipulation.
- The diff algorithm **detects exactly what changed** on the page and changes only that, rather than re-rendering the whole tree.

---

## 14.7 Concurrent rendering

**Concurrent rendering** is a feature of React that allows the browser to continue rendering the rest of the application while a component is being updated. This can improve the user experience by providing smoother animations and reducing the perceived time to load the application.

**Async mode vs Concurrent mode:** Async mode is an experimental feature that allows React to schedule updates and render components asynchronously, improving performance by reducing the number of updates processed at the same time. Concurrent mode is a feature that allows React to work in an asynchronous way.

---
---

# PART 15 — Build Tools, Bundlers and npm

*This part explains what `create-react-app` hides from you. Understanding it makes you a much stronger React developer.*

## 15.1 Getting React without a build tool — CDN

**A CDN (Content Delivery Network) is a network of servers that delivers content to users.** Both React and ReactDOM are available over a CDN.

```html
<body>
  <div id="root"></div>
</body>

<script crossorigin src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
<script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
<!-- React superpowers come from here -->

<script>
  const heading = React.createElement("h1", {}, "Namaste Everyone");
  const root = ReactDOM.createRoot(document.getElementById("root"));
  root.render(heading);
</script>
```

> **React will overwrite everything inside `root` and replace it with whatever is given inside `render`.**

**Why CDN is a great place to host images too:** CDN is faster. It caches the image. It returns very fast and has 100% uptime. It optimises images (they are already optimized when put into the CDN).

**But using CDN links is not a good way for a real app.** We want React in our `node_modules`:
```bash
npm install react
```

---

## 15.2 npm and package.json

**npm** is a package manager. (Fun fact: **npm doesn't actually stand for "Node Package Manager"** — it stands for everything else. The joke version: "No Problem Man".)

```bash
npm init          # creates a package.json file
npm init -y       # skips all the questions
```

We use npm because we want a lot of packages in our React app.

### The caret and the tilde
```json
"devDependencies": {
  "parcel": "^2.8.2"      // ^ = caret
}
```
With the **caret (`^`)**, your project will automatically accept minor version updates. **`package-lock.json`** tells you which *exact* version of the library you are actually using.

---

## 15.3 Bundlers

To make an app production-ready, we should:
1. **Minify** our files (remove console logs, bundle things up)
2. Have a **server** to run things

**"Minify → Optimization → Clean console → and Bundle"**

In React, to get these external capabilities we use **BUNDLERS**:
- **Webpack** (what `create-react-app` uses, along with **Babel**)
- **Vite**
- **Parcel**
- Also: rollup, browserify

Most bundlers do the same job. Bundlers are npm packages.

### Bundling
**Bundling is the process of combining multiple JavaScript files into a single file.** This is done to reduce the number of network requests needed to load an application and to improve performance. The bundle is responsible for loading the entire app at once on the webpage.

---

## 15.4 Parcel — a bundler in depth

### Installing
```bash
npm install -D parcel
```
- `-D` = **dev dependency**, because we want it on our developer machine only.

### Igniting your app
```bash
npx parcel index.html
```
- `npx` means **"execute using npm"**.
- `index.html` is the **entry point**.

Press enter and a mini-server is created for you at something like `localhost:1234`. **Parcel gave a server to us. Parcel ignited our app.**

### Building for production
```bash
npx parcel build index.html
```
This minifies your files and **builds all production files to the `dist` folder**.

### The `type="module"` requirement
A normal browser script doesn't understand `import`. So you must tell the browser you are not using a normal script tag:
```html
<script type="module" src="App.js"></script>
```
**You cannot import and export inside a plain script tag. Modules can import and export.**

### Hot Module Reload (HMR)
**HMR means Parcel keeps track of all the files you are updating.**

**How does HMR work?** There is a **File Watcher Algorithm** (written in **C++**). It keeps track of all the files that are changing in realtime and it tells the server to reload. This is all done by Parcel.

### The folders Parcel creates
- **`.parcel-cache`** — Parcel needs some space in your project, so it creates this. **Put it in `.gitignore`.**
- **`dist`** — keeps the minified files for you.

### The full list of Parcel features

- HMR — Hot Module Reloading
- File Watcher algorithm — written in C++
- Bundling
- Minify code
- Cleaning our code
- Dev and production builds
- Super fast build algorithm
- **Image optimization** *(Q: What takes a long time to load in a website? A: Media — images. Parcel does image optimization.)*
- Caching while development
- Compression
- Compatible with older browser versions
- **HTTPS on dev** — `npx parcel index.html --https` (sometimes you need to test on https because something only works there)
- Port number
- Consistent Hashing Algorithm
- **Zero Config**
- Tree Shaking

**Finally: "Parcel is a beast."**

### Tree Shaking
**Tree shaking means removing unwanted code.**

Suppose your app imports a library that has 20 helper functions. Normally all 20 functions would come into your bundle. But in your app you may only use 1 or 2 of them. **Parcel will ignore all the unused code.**

---

## 15.5 Transitive dependencies

Our package manager handles and takes care of the transitive dependencies of our code.

If you have to build a production-ready app that uses all the optimizations (minify, cleaning, bundling, compression, consistent hashing etc.), you can't do this alone. You need dependencies. **And those dependencies are themselves dependent on many other dependencies.**

```
Our App
   ├── REACT
   └── PARCEL
         ├── Dependency 1
         └── Dependency 2
               ├── D11
               ├── D12
               │     ├── D121
               │     ├── D122
               │     └── D123
               └── D13
```

That whole tree is your app.

---

## 15.6 Browser compatibility — browserslist and polyfills

### The problem
ES6 is a newer version of JavaScript. If someone is on a 1999-era browser, that browser won't understand `const`, `new Promise`, and so on.

### Polyfill
**To make older browsers understand our new code, the new code is converted into older code which the browser can understand — this is called a polyfill.**

### Babel
**Babel is a JavaScript package/library used to convert code written in newer versions of JS (ECMAScript 2015, 2016, 2017 etc.) into code that can be run in older JS engines.** Babel does this conversion automatically. Babel comes along with Parcel.

Babel is a **JavaScript compiler**.

### browserslist
**Q: How do I make my app compatible with older browsers?**

**A:** There is a package called **`browserslist`**, and Parcel gives it to us automatically. Browserslist makes our code compatible with a lot of browsers. (See `browserslist.dev`.)

In `package.json`:
```json
"browserslist": [
  "last 2 versions"
]
```
This means Parcel will make sure your app works in the last 2 versions of all available browsers. (~74% support.)

If you only care about Chrome:
```json
"browserslist": [
  "last 2 Chrome versions"
]
```
(~16% support.)

---

## 15.7 npm scripts

To run our app, the command is `npx parcel index.html`. We don't always want to type that. So we build a **script** inside `package.json`:

```json
"scripts": {
  "start": "parcel index.html",
  "build": "parcel build index.html",
  "test": "jest"
}
```

Then:
```bash
npm run start
```
(shortcut: `npm start`)

```bash
npm run build
```

> Note: `npx` ≈ `npm run`.

---

## 15.8 Removing console logs in production

Console logs are **not** removed automatically by Parcel. You have to configure your project. There is a package that helps:

```bash
npm install babel-plugin-transform-remove-console
```

Before installing, create a `.babelrc` file for configuration:
```json
{
  "plugins": [
    ["transform-remove-console", { "exclude": ["error", "warn"] }]
  ]
}
```
Then run `npm run build` and all `console.log` calls will be removed (but `console.error` and `console.warn` are kept).

---

## 15.9 Code splitting

**Code splitting is a technique that allows you to split your application's JavaScript code into smaller chunks.** This can improve performance by only loading the code needed for the current page or component. It is usually used in combination with a bundler like webpack.

### Code splitting improves
1. The performance of the app
2. The impact on memory
3. The downloadable kilobyte size

### `React.lazy`
The best way to do code splitting is through the dynamic **`import()`** syntax. The `React.lazy` function allows us to render a dynamic import as a regular component.

**Before:**
```jsx
import ExampleComponent from './ExampleComponent';

function MyComponent() {
  return (
    <div>
      <ExampleComponent />
    </div>
  );
}
```

**After:**
```jsx
const ExampleComponent = React.lazy(() => import('./ExampleComponent'));

function MyComponent() {
  return (
    <div>
      <ExampleComponent />
    </div>
  );
}
```

### With Suspense and Error Boundaries
If any module fails to load — for example, due to network failure — we get an error. We handle these with **Error Boundaries**.

```jsx
import React, { Suspense } from 'react';
import MyErrorBoundary from './MyErrorBoundary';

const ExampleComponent = React.lazy(() => import('./ExampleComponent'));

const MyComponent = () => (
  <div>
    <MyErrorBoundary>
      <Suspense fallback={<div>Loading</div>}>
        <section>
          <ExampleComponent />
          <ExampleComponent />
        </section>
      </Suspense>
    </MyErrorBoundary>
  </div>
);
```

### Route-based code splitting
**Route-based code splitting** splits your JavaScript into smaller chunks based on the routes in your application, only loading the code needed for the current page.

```jsx
import React, { Suspense, lazy } from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

const Home = lazy(() => import('./Home'));
const About = lazy(() => import('./About'));

function App() {
  return (
    <Router>
      <Suspense fallback={<div>Loading...</div>}>
        <Switch>
          <Route path="/" exact component={Home} />
          <Route path="/about" component={About} />
        </Switch>
      </Suspense>
    </Router>
  );
}
```

---

## 15.10 Microservices — where React fits

In older days there was a single big application. Everything — APIs, SMS, notifications, UI, JSP pages — was in the same project. If you had to change one button, you had to deploy the whole application. It was a mess. **This architecture was known as a monolith.**

### Separation of concern
Now, instead of one big project, we have small separate projects:

| Port | Project | Language |
|---|---|---|
| /1234 | UI project | React |
| /1235 | Backend API | Java |
| /1236 | Notification project | Python |
| /1237 | Logs | Python |
| /1238 | Authentication project | Go |

These are separate projects. **Separation of concern / single responsibility** applies. The tools and languages used in each project depend on the use case. All these projects are deployed on different ports but under the same domain name.

---
---

# PART 16 — Class Components and the Lifecycle (Legacy)

> **Read this section for understanding legacy codebases and for interviews.** In modern React code, the concept of lifecycle methods has been replaced by hooks.
>
> **NB: Never directly compare React lifecycle methods with functional components.** They are different mental models.

## 16.1 Why class components still matter

Class components were less maintainable, had more code and were a little messy. **They are no longer commonly used.** Developers can do almost everything using functional components now.

But: a functional component is, at the end, just a normal JS function. Similarly, **class-based components are just normal JS classes**.

## 16.2 Side by side

| CLASS BASED COMPONENT (ProfileClass.js) | FUNCTIONAL COMPONENT (ProfileFunc.js) |
|---|---|
| ```jsx
import React from "react";
class Profile extends React.Component {
  render() {
    return <h1>Profile</h1>;
  }
}
export default Profile;
``` | ```jsx
const Profile = () => {
  return (
    <h1>Profile</h1>
  );
};
export default Profile;
``` |

Annotated:
- `import React from "react";` — `React.Component` comes from here
- `class Profile extends React.Component {` — `class` is the keyword, `Profile` is the component name. You have to tell React that this is a **class component**, not a normal JavaScript class, by extending `React.Component`.
- `render() { ... }` — return some JSX. **You can't create a class component without a `render` method.** Whatever you return from it will be injected into the DOM.
- **`render()` is the only mandatory method for class-based components.**

---

## 16.3 Props in class components

```jsx
<ProfileClass name={"Ashraya"} xyz={"abc"} />
```

In a class component we have the **`this`** keyword. React collects all the props and attaches them to `this`:

```jsx
<h2>Name: {this.props.name}</h2>
<h2>xyz: {this.props.xyz}</h2>
```

---

## 16.4 State in class components

```jsx
class Profile extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      count: 0,
      count2: 0,
    };
  }

  render() {
    return (
      <>
        <h2>Count: {this.state.count}</h2>
        <h2>Count2: {this.state.count2}</h2>
        <button onClick={() => {
          this.setState({
            count: 1,
            count2: 2,
          });
        }}>Set Count</button>
      </>
    );
  }
}
```

- `constructor(props) { super(props); }` creates and initializes the component's state.
- **`super(props)` is necessary** because it passes the received props to the constructor of the base component class, allowing the component to access its properties.
- The constructor function is called **only once**, when the component is first created and initialized, making it the ideal place to set the initial state using `this.state = {...}`.
- **We do not mutate state directly.** Always use `this.setState(...)`.

---

## 16.5 The React Constructor

**The constructor is a method used to initialize an object's state in a class.** It is automatically called during the creation of an object.

```jsx
constructor(props) {
  super(props);
}
```

In React, constructors are mainly used for **two** purposes:
1. **Initialising** the local state of the component by assigning an object to `this.state`.
2. **Binding event handler** methods that occur in your component.

> **Note:** If you neither initialize state nor bind methods for your React component, **there is no need to implement a constructor** at all.

The constructor uses `this.state` to assign initial values; all other methods must use `setState()`.

### Full example
```jsx
import React, { Component } from 'react';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: 'Topperworld.in'
    };
    this.handleEvent = this.handleEvent.bind(this);
  }

  handleEvent() {
    console.log(this.props);
  }

  render() {
    return (
      <div className="App">
        <h2>React Constructor Example</h2>
        <input type="text" value={this.state.data} />
        <button onClick={this.handleEvent}>Please Click</button>
      </div>
    );
  }
}

export default App;
```

---

## 16.6 The component lifecycle

In React, every component creation process involves various lifecycle methods. These are termed the **component's lifecycle**. The lifecycle is divided into **4 phases**:

```
Initial Phase  →  Mounting Phase  →  Updating Phase  →  Unmounting Phase
```

### Phase 1 — Initial Phase
This is the birth phase of the component's lifecycle. The component starts its journey towards the DOM. **The initial phase occurs only once.**

- **`getDefaultProps()`** — used to specify the default value of `this.props`. Invoked before the creation of the component or any props from the parent are passed onto it.
- **`getInitialState()`** — used to specify the default value of `this.state`. Invoked before the creation of the component.

### Phase 2 — Mounting Phase
In this phase, an instance of the component is created and inserted into the DOM.

- **`componentWillMount()`** — Invoked immediately **before** a component gets rendered into the DOM. If you call `setState()` inside this method, the component will not re-render.
- **`render()`** — Defined in every component. Responsible for returning a single root HTML node element.
- **`componentDidMount()`** — Invoked immediately **after** the component gets rendered and placed on the DOM. Now you can do any DOM querying operations. **This is the best place to make an API call.**

### Phase 3 — Updating Phase
The main aim of this phase is to ensure that the component displays the latest version of itself.

- **`componentWillReceiveProps()`** — Invoked when a component receives new props. If you want to update state in response to prop changes, you should compare `this.props` and `nextProps` and perform the state transition using `this.setState()`.
- **`shouldComponentUpdate()`** — Invoked when the component decides on any changes/updates to the DOM. It returns a **boolean** indicating whether the component should update. It allows you to control the component's behaviour.
- **`componentWillUpdate()`** — Invoked just before the component update occurs. Here you **can't** change component state by invoking `this.setState()`. **It will not be called if `shouldComponentUpdate()` returns false.**
- **`render()`** — Invoked to examine `this.props` and `this.state` and return one of: React elements, arrays and fragments, boolean or null, string, or number.
- **`componentDidUpdate()`** — Invoked immediately after the component update occurs.

### Phase 4 — Unmounting Phase
The final phase, called when the component instance is destroyed and unmounted from the DOM.

- **`componentWillUnmount()`** — Invoked immediately before a component is destroyed and unmounted permanently. It performs the necessary cleanup-related tasks. **If a component instance is unmounted, you cannot mount it again.**

---

## 16.7 The modern lifecycle order (React 16+)

### Mounting order
1. `constructor()`
2. `static getDerivedStateFromProps()`
3. `render()`
4. `componentDidMount()`

### Updating
- `shouldComponentUpdate()`
- `render()`
- `getSnapshotBeforeUpdate()`
- `componentDidUpdate()`

### Unmounting
- `componentWillUnmount()`

### Deprecated in React v16
- `componentWillMount`
- `componentWillReceiveProps`
- `componentWillUpdate`

### The newer methods explained
- **`getDerivedStateFromProps()`** — Provides a way to synchronize a component's internal state with its props. Called **before `render()`**, it allows you to update internal state based on changes in props. It is the replacement for `componentWillReceiveProps()`.
- **`getSnapshotBeforeUpdate()`** — Captures some information from the DOM **before it is potentially changed**. Called right before the browser updates the DOM, it allows you to capture the current scroll position or other information you might want to use later.

---

## 16.8 A complete lifecycle demonstration

```jsx
import React, { Component } from 'react';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hello: "Topperworld" };
    this.changeState = this.changeState.bind(this);
  }

  render() {
    return (
      <div>
        <h1>ReactJS component's lifecycle</h1>
        <h3>Hello {this.state.hello}</h3>
        <button onClick={this.changeState}>Click here!</button>
      </div>
    );
  }

  componentWillMount() {
    console.log('component will Mount!');
  }

  componentDidMount() {
    console.log('Component Did Mount!');
  }

  changeState() {
    this.setState({ hello: "All!! - Its a great reactjs tutorial." });
  }

  componentWillReceiveProps(newProps) {
    console.log("Component will Receive Props!");
  }

  shouldComponentUpdate(newProps, newState) {
    return true;
  }

  componentWillUpdate(nextProps, nextState) {
    console.log('component will Update');
  }

  componentDidUpdate(prevProps, prevState) {
    console.log('ComponentDidUpdate');
  }

  componentWillUnmount() {
    console.log('Component will unmount!');
  }
}

export default App;
```

---

## 16.9 Making an API call in a class component

**The best place to make an API call in a class component is `componentDidMount()`.**

This is because during the mounting phase: (1) `constructor()`, then (2) `render()`, and finally (3) `componentDidMount()`.

```jsx
class ApiDataFetchExample extends React.Component {
  state = { data: [], loading: true, error: null };

  componentDidMount() {
    this.fetchData();
  }

  fetchData = () => {
    fetch("https://api.example.com/data")
      .then(response => response.json())
      .then(data => this.setState({ data, loading: false }))
      .catch(error => this.setState({ error, loading: false }));
  }
}
```

### With async/await
```jsx
class Profile extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      userInfo: {
        name: "",
        location: "",
      }
    };
    console.log("Child-Constructor");
  }

  async componentDidMount() {
    const data = await fetch("https://api.github.com/users/Ashrayaa");
    const json = await data.json();
    this.setState({ userInfo: json });
    console.log("Child-componentDidMount");
  }

  render() {
    console.log("Child-render");
    return (
      <>
        <h1>Name: {this.state.userInfo.name}</h1>
        <img src={this.state.userInfo.avatar_url} />
        <h2>Location: {this.state.userInfo.location}</h2>
      </>
    );
  }
}
```

### The sequence when the API call is async
1. Parent — constructor
2. Parent — render
3. Child — constructor
4. Child — render
5. DOM is updated
6. json is logged in the console
7. **Parent — componentDidMount** *(called BEFORE the child's, because the child's is awaiting the API)*
8. Child — componentDidMount
9. Child — render *(again)*

`setState` triggers the next render. It triggers the reconciliation process. So the child renders once again when it has the data. **This re-render cycle is known as "UPDATING".**

### Summary of the three key methods
- **`componentDidMount`** is called after the **first** render.
- **`componentDidUpdate`** is called after **every subsequent** render.
- **`componentWillUnmount`** is called before the component is removed from the DOM.

---

## 16.10 `componentDidUpdate` vs the useEffect dependency array

In a functional component, we use a dependency array to say when the effect should run:
```jsx
useEffect(() => {
  // API call
}, [count, count2]);
```
This means: whenever `count` **or** `count2` gets updated, run this.

In class-based components, this was done like the following — **which is hectic**:
```jsx
componentDidUpdate(prevProps, prevState) {
  if (
    this.state.count !== prevState.count ||
    this.state.count2 !== prevState.count2
  ) {
    // code
  }
}
```

This is one of the clearest reasons hooks won.

---

## 16.11 React Component API

React components have a top-level API that makes code individual and reusable. It includes methods for creating elements, transforming elements, and fragments.

### `setState()`
Used to update the state of the component. **The method does not always replace the state immediately — it only adds changes to the original state.** It is the primary method used to update the UI in response to event handlers and server responses.

```
this.setState(object newState [, function callback]);
```

```jsx
import React, { Component } from 'react';

class App extends React.Component {
  constructor() {
    super();
    this.state = { msg: "Welcome" };
    this.updateSetState = this.updateSetState.bind(this);
  }

  updateSetState() {
    this.setState({ msg: "It's the best tutorial" });
  }

  render() {
    return (
      <div>
        <h1>{this.state.msg}</h1>
        <button onClick={this.updateSetState}>SET STATE</button>
      </div>
    );
  }
}

export default App;
```

**The `setState()` callback:** the callback function passed as a second argument is called **after** the state has been updated and the component has re-rendered. It can be used to perform additional actions, such as sending a network request, that depend on the updated state.

> ⚠️ **What happens if you use `setState()` in the constructor?** It will cause the component to re-render before it is added to the DOM. This causes unexpected behavior and should be avoided. Instead, initialize state from the constructor's props and use `setState` in `componentDidMount`.

### `forceUpdate()`
This method allows you to update the component **manually**.

```
Component.forceUpdate(callback);
```

```jsx
import React, { Component } from 'react';

class App extends React.Component {
  constructor() {
    super();
    this.forceUpdateState = this.forceUpdateState.bind(this);
  }

  forceUpdateState() {
    this.forceUpdate();
  }

  render() {
    return (
      <div>
        <h1>Example to generate a random Number</h1>
        <h3>Random number: {Math.random()}</h3>
        <button onClick={this.forceUpdateState}>ForceUpdate</button>
      </div>
    );
  }
}

export default App;
```
Each time you click ForceUpdate, a new random number is displayed.

### `findDOMNode()`
For DOM manipulation, you need `ReactDOM.findDOMNode()`. This method allows you to find or access the underlying DOM node.

```
ReactDOM.findDOMNode(component);
```

```jsx
import React, { Component } from 'react';
import ReactDOM from 'react-dom';

class App extends React.Component {
  constructor() {
    super();
    this.findDOMNodeHandler1 = this.findDOMNodeHandler1.bind(this);
    this.findDOMNodeHandler2 = this.findDOMNodeHandler2.bind(this);
  }

  findDOMNodeHandler1() {
    var myDivOne = document.getElementById("myDivOne");
    ReactDOM.findDOMNode(myDivOne).style.color = "red";
  }

  findDOMNodeHandler2() {
    var myDivTwo = document.getElementById("myDivTwo");
    ReactDOM.findDOMNode(myDivTwo).style.color = "blue";
  }

  render() {
    return (
      <div>
        <h1>ReactJS Find DOM Node Example</h1>
        <button onClick={this.findDOMNodeHandler1}>FIND_DOM_NODE1</button>
        <button onClick={this.findDOMNodeHandler2}>FIND_DOM_NODE2</button>
        <h3 id="myDivOne">JTP-Node1</h3>
        <h3 id="myDivTwo">JTP-Node2</h3>
      </div>
    );
  }
}

export default App;
```
Once you click the button, the color of the node changes.

---
---

# PART 17 — Refs, Fragments, Portals, HOCs and Context

## 17.1 Refs

**"Refs" is shorthand for "references".** It is an attribute which makes it possible to store a reference to a particular DOM node or React element. It provides a way to access React DOM nodes or React elements and to interact with them.

### When to use refs
- When we need **DOM measurements** such as managing focus, text selection, or media playback.
- For triggering **imperative animations**.
- When **integrating with third-party DOM libraries**.
- It can also be used in callbacks.

### When NOT to use refs
- Avoid using refs for anything that can be done **declaratively**. Instead of using `open()` and `close()` methods on a Dialog component, you should pass an `isOpen` prop to it.
- **You should avoid overuse of refs.**

### Creating refs — the class way
Refs can be created using **`React.createRef()`**. Assign it to a React element via the `ref` attribute. It is commonly assigned to an instance property when the component is created, and can then be referenced throughout the component.

```jsx
class MyComponent extends React.Component {
  constructor(props) {
    super(props);
    this.callRef = React.createRef();
  }

  render() {
    return <div ref={this.callRef} />;
  }
}
```

### Accessing refs
When a ref is passed to an element inside the render method, a reference to the node can be accessed via the **`current`** attribute of the ref:
```jsx
const node = this.callRef.current;
```

### The `current` property — three rules
- When the `ref` attribute is used on an **HTML element**, the ref created with `React.createRef()` receives the underlying **DOM element** as its `current` property.
- If the `ref` attribute is used on a **custom class component**, the ref object receives the **mounted instance** of the component as its `current` property.
- **The `ref` attribute cannot be used on a function component** because they don't have instances. *(Use `forwardRef` or, in React 19, ref-as-a-prop.)*

### Callback refs
There is another way to use refs, called **callback refs**, which gives more control over when refs are set and unset. Instead of creating a ref object, you pass a callback function to the `ref` attribute:

```jsx
<input type="text" ref={element => this.callRefInput = element} />
```

The callback function stores a reference to the DOM node in an instance property, which can then be accessed elsewhere:
```jsx
this.callRefInput.value
```

### Forward refs

**A forward ref is a way to pass a ref through a component to a child component.** It allows you to access the ref of a child component from the parent component.

```jsx
import React, { forwardRef } from 'react';

const ChildComponent = forwardRef((props, ref) => {
  return <input type="text" ref={ref} />;
});

function ParentComponent() {
  const inputRef = React.useRef(null);

  function handleClick() {
    inputRef.current.value = "Hello World!";
  }

  return (
    <div>
      <ChildComponent ref={inputRef} />
      <button onClick={handleClick}>Update Input</button>
    </div>
  );
}

export default ParentComponent;
```

The `forwardRef` function takes a component and returns a new component that **can accept a `ref` as a prop**. The `ParentComponent` has a ref object `inputRef` that is passed as a prop to the `ChildComponent` using the `ref` attribute. Inside the child, the `ref` prop is passed as a **second argument** to the component function, and from there to the input element.

When the button is clicked, `handleClick` updates the value of the input field by accessing its `value` property via the ref object. **This way, the ref object can be passed through the component hierarchy to access elements deep down in the tree.**

> `forwardRef` is also how you create a **props proxy** for a Higher-Order Component — it lets you pass props through to the wrapped component, preserving the original component's props.

> **React 19 update:** function components can now accept `ref` directly as a normal prop. `forwardRef` still works, but is **no longer required**. See Part 23.

---

## 17.2 Fragments

### The problem fragments solve

When you want to render something, you use `render()` inside a component. This render method can return single or multiple elements. If you want to return **multiple** elements, historically the render method required a `div` tag wrapping the entire content.

```jsx
class App extends React.Component {
  render() {
    return (
      <div>                            {/* this div is only here to satisfy React */}
        <h2>Hello world</h2>
        <p>Welcome</p>
      </div>
    );
  }
}
```

**This extra node in the DOM sometimes results in wrong formatting of your HTML output.**

> **The rule:** JSX expressions must have **one parent element**.

### The solution
React introduced **fragments**. **Fragments allow you to group a list of children without adding extra nodes to the DOM.**

```jsx
<React.Fragment>
  <h2>child1</h2>
  <p>child2</p>
</React.Fragment>
```

```jsx
class App extends React.Component {
  render() {
    return (
      <React.Fragment>
        <h2>Hello World</h2>
        <p>Welcome to TopperWorld</p>
      </React.Fragment>
    );
  }
}
```

`React.Fragment` is a component exported by React (`import React from "react";`).

### Why use fragments?
1. **It makes execution of code faster** compared to a `div` tag.
2. **It takes less memory.**
3. It doesn't add an extra node to the DOM — the rendered HTML is cleaner and more efficient, especially when a component renders a list of items.
4. **It helps with accessibility** because it doesn't create an unnecessary wrapper element around the content.

### The short syntax
There is a shorthand for declaring fragments. It looks like an empty tag: use `<>` and `</>` instead of `<React.Fragment>`.

```jsx
class Columns extends React.Component {
  render() {
    return (
      <>
        <h2>Hello</h2>
        <p>Welcome to Topperworld</p>
      </>
    );
  }
}
```

> ⚠️ **But you can't pass styles or any props to the empty-bracket shorthand.**

### Keyed fragments
**The shorthand syntax does not accept a `key` attribute.** `key` is the only attribute that can be passed to a fragment. You need a key when mapping a collection to an array of fragments — for example, to create a description list. If you need to provide keys you **must** use the explicit `React.Fragment` syntax.

```jsx
function Glossary(props) {
  return (
    <React.Fragment>
      {props.items.data.map(item => (
        // Without 'key', React will give a warning
        <React.Fragment key={item.id}>
          <h2>{item.name}</h2>
          <p>{item.url}</p>
          <p>{item.description}</p>
        </React.Fragment>
      ))}
    </React.Fragment>
  );
}
```

### Can you nest fragments inside fragments?
**Yes.** You can nest `React.Fragment` components inside other `React.Fragment` components.

```jsx
import React from 'react';

const jsx = (
  <>
    <ChildA />
    <>
      <ChildB />       {/* Child B & C are siblings and will be grouped */}
      <ChildC />       {/* together without adding an extra node to the DOM */}
    </>
    <ChildD />
  </>
);
```

### An `AppLayout` using fragments
```jsx
import React from 'react';

const AppLayout = () => {
  return (
    <React.Fragment>
      <Header />
      <Body />
      <Footer />
    </React.Fragment>
  );
};
```

---

## 17.3 Portals

**React portals provide a way to render children into a DOM node that exists outside the DOM hierarchy of the parent component.**

It is very tricky to render a child component outside of its parent component's hierarchy. Portals break the convention where a component needs to render as a new element and follow a parent-child hierarchy.

### Syntax
```jsx
ReactDOM.createPortal(child, container)
```
- **`child`** — a React component or fragment that can be rendered in the DOM.
- **`container`** — a reference to the element present in the HTML page into which the child element will be rendered.

### Features of portals
- It uses **React version 16** and its official API for creating portals.
- It has a fallback for React version 15.
- It transports its children component into a new React portal which is **appended by default to `document.body`**.
- It can also target a **user-specified DOM element**.
- It supports **server-side rendering**.
- It supports returning arrays.
- It **doesn't produce any DOM mess**.
- It has **no dependencies** — minimalistic.
- Flexible component rendering, improved performance, integration with third-party libraries, encapsulation and isolation.

### When to use portals
1. **Modals**
2. **Tooltips**
3. **Floating menus**
4. **Widgets**

### A complete portal example

**App.js**
```jsx
import React, { Component } from 'react';
import './App.css';
import PortalDemo from './PortalDemo.js';

class App extends Component {
  render() {
    return (
      <div className="App">
        <PortalDemo />
      </div>
    );
  }
}

export default App;
```

**PortalDemo.js**
```jsx
import React from 'react';
import ReactDOM from 'react-dom';

function PortalDemo() {
  return ReactDOM.createPortal(
    <h1>Portals Demo</h1>,
    document.getElementById('portal-root')
  );
}

export default PortalDemo;
```

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <link rel="shortcut icon" href="%PUBLIC_URL%/favicon.ico" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="theme-color" content="#000000" />
  <title>React App</title>
</head>
<body>
  <noscript>You need to enable JavaScript to run this app</noscript>
  <div id="root"></div>
  <div id="portal-root"></div>
</body>
</html>
```

---

## 17.4 Dialogs (a portal use case)

**Dialogs are modal components that overlay the main content to display important messages, notifications or user interactions.**

```jsx
import React from 'react';
import ReactDOM from 'react-dom';

const DialogExample = ({ isOpen, onClose, children }) => {
  if (!isOpen) return null;

  return ReactDOM.createPortal(
    <div className="dialog-overlay">
      <div className="dialog-content">
        <button className="close-button" onClick={onClose}>
          Close
        </button>
        {children}
      </div>
    </div>,
    document.getElementById('dialog-root')
  );
};

export default DialogExample;
```

When you click the "Open Dialogue" button, "This is a Dialog / Dialog content goes here" will be displayed as an overlay.

---

## 17.5 Higher-Order Components (HOC)

**A higher-order component (HOC) is a function that takes a component as an argument and returns a new component with additional functionality.**

HOCs are used to **reuse component logic**, such as authentication or performance optimization.

```jsx
const NewComponent = higherOrderComponent(WrappedComponent);
```

### Example

**HOC.js**
```jsx
import React, { Component } from 'react';

export default function HOC(HOCComponent) {
  return class extends Component {
    render() {
      return (
        <div>
          <HOCComponent />
        </div>
      );
    }
  };
}
```

**App.js**
```jsx
import React, { Component } from 'react';
import HOC from './HOC';

class App extends Component {
  render() {
    return (
      <div>
        <h2>HOC Example</h2>
        JavaTPoint provides the best CS Tutorials
      </div>
    );
  }
}

App = HOC(App);

export default App;
```

### Render hijacking
**Render hijacking in React is a technique that allows you to modify the rendered output of a component by wrapping it in another component.** The wrapping component can then add or remove elements, change the styles, or modify the behavior of the original component. HOCs are how this is done.

---

## 17.6 The Context API

**The Context API allows passing data through the component tree without passing props down manually at every level.**

It provides a way for components to access data that is **"global" to the component tree**, such as a user's authentication status or a theme. It provides a way to create a **global state** that can be accessed and modified by components at any level.

### The four parts of the Context API

**1. `React.createContext`** — creates a context object.
```jsx
const MyContext = React.createContext(defaultValue);
```

**2. `Context.Provider`** — every Context object has a Provider React component which allows consuming components to subscribe to context changes.
```jsx
<MyContext.Provider value={/* some value */} />
```

**3. `Context.Consumer`** — a React component which subscribes to context changes. It allows us to access the context within a function.
```jsx
<MyContext.Consumer>
  {value => /* render something based on the context value */}
</MyContext.Consumer>
```

**4. `class.contextType`** — the `contextType` property on a class is used to assign a context object created by `React.createContext()`. It allows you to consume the closest current value of that context using `this.context`.

### Class-based example
```jsx
import React, { Component } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

const BtnColorContext = React.createContext("btn btn-dark yellow");

class App extends Component {
  render() {
    return (
      <BtnColorContext.Provider value='btn btn-info'>
        <Button />
      </BtnColorContext.Provider>
    );
  }
}

function Button(props) {
  return (
    <div className="container">
      <ThemedButton />
    </div>
  );
}

class ThemedButton extends Component {
  static contextType = BtnColorContext;

  render() {
    return <button className={this.context}>Welcome to JavaTpoint</button>;
  }
}
```

### The modern hook-based approach
```jsx
import React, { createContext, useContext, useState } from 'react';

// 1. Create the context
const MyContext = createContext();

// 2. Create a provider component
function MyProvider({ children }) {
  const [state, setState] = useState(initialState);

  return (
    <MyContext.Provider value={{ state, setState }}>
      {children}
    </MyContext.Provider>
  );
}

// 3. Use the context in a child component
function ChildComponent() {
  const { state, setState } = useContext(MyContext);
  // Access and update the state
  return <div>{state}</div>;
}
```

The `MyProvider` component **wraps** the child components that need access to the shared state. The state is stored in the provider's local state using `useState()`. The `ChildComponent` consumes the context using the `useContext()` hook, allowing it to access the state and modify it.

> ⚠️ **Common mistake:** prop drilling.
>
> | ❌ DON'T | ✅ DO |
> |---|---|
> | Passing props through 4+ layers that don't use them | Use Context or component composition |

---
---

# PART 18 — State Management

## 18.1 Why state management?

**State management in a React application refers to the process of managing and organizing the application's state**, which includes data, UI states, and other relevant information.

As the application grows in complexity, managing state becomes more challenging, and **proper state management techniques are necessary to ensure a predictable and maintainable application.**

There are different approaches:
1. **React Context API** (built in) — see Part 17.6
2. **Redux**
3. Alternatives: **Mobx, Apollo, Unstated-next, Zustand**

---

## 18.2 MVC vs Flux

### MVC (Model View Controller)
MVC is an architectural pattern used for developing the user interface.

- **Model** — responsible for maintaining the behaviour and data of an application.
- **View** — used to display the model in the user interface.
- **Controller** — acts as an interface between the Model and the View. It takes user input, manipulates the data, and causes the view to update.

```
MODEL ──UPDATES──▶ VIEW ──SEES──▶ USER ──USES──▶ CONTROLLER ──MANIPULATES──▶ MODEL
```

### Flux
**Flux is an application architecture that Facebook uses for building client-side web applications.** It is designed to be used with React and it provides a **unidirectional data flow**, where data is passed down through components in a hierarchical structure.

Flux architecture has 3 major roles in dealing with data:
1. **Dispatcher**
2. **Store**
3. **Views**

```
Action ──▶ Dispatcher ──▶ Store ──▶ View ──▶ Action  (loop)
```

- **Action Creator** — a helper method that creates an action from its parameters, assigns it a type, and then provides it to the dispatcher.
- **Dispatcher** — acts as a central hub. It sends every action to all stores via the callbacks that have registered with it.
- **Store** — updates itself in response to an action, then emits a change event to alert the controller view.
- **Controller view** — listens for change events, retrieves new data from the stores, and provides the new data to their descendants in the component tree.

### MVC vs Flux — the comparison

| | MVC | Flux |
|---|---|---|
| 1 | Introduced in **1976** | Introduced just a few years ago |
| 2 | Supports **bi-directional** data flow model | Supports **uni-directional** data flow model |
| 3 | **Data binding** is the key | **Events or actions** are the key |
| 4 | It is **synchronous** | It is **asynchronous** |
| 5 | Controllers handle everything | **Store** handles all logic |
| 6 | It is **hard to debug** | It is **easy to debug** |
| 7 | Difficult to understand as project size increases | Easy to understand |
| 8 | Maintainability is difficult as the project scope grows huge | Maintainability is easy and it reduces run-time errors |
| 9 | Testing of the application is **difficult** | Testing of the application is **easy** |
| 10 | Scalability is complex | It can be easily scaled |

---

## 18.3 Redux

**Redux is a predictable state container for JavaScript applications.** It helps you write apps that behave consistently, run in different environments (client, server, native) and are easy to test.

- Redux is a **state management tool**.
- Redux can be used with **any** JavaScript framework — it is not React-specific.
- Redux stores the state of the application, and components can access the state from the state store.
- It provides a **centralised, predictable and immutable state container**.

**Redux was inspired by Flux.** The differences:
1. Redux does **not** have the dispatcher concept.
2. Redux has **only one Store**, whereas Flux has many stores.
3. Action objects are received and handled **directly by the Store**.

### The Redux architecture
```
Store ──contains──▶ State ──defines──▶ UI ──triggers──▶ Actions ──sent to──▶ Reducer ──updates──▶ Store
```

---

## 18.4 The three principles of Redux

**1. Single Source of Truth**
The state of your whole application is stored in an object tree within a **single store**. A single state tree makes it easier to debug or inspect an application. It gives you a faster development cycle by enabling you to persist your app's navigation state.

**2. State is read-only**
The only way to change the state is to **initiate an action** — an object describing what happened. This ensures that no events like network callbacks or views can change state directly. Actions are just plain objects, so they can be logged.

**3. Changes are made with pure functions**
To specify how actions transform the state tree, you write **pure reducers**. The user can return new state objects instead of mutating previous state.

---

## 18.5 The core concepts of Redux

### Store
**The Redux store holds the application state.** It is created using the `createStore()` function from the Redux library and manages the state and state updates.

A store is a place where the entire state of your application lives. It manages the status of the application and has a dispatch function. **It is like a brain, responsible for all moving parts in Redux.**

Store methods:
- **`getState()`** — returns the current state
- **`dispatch()`** — dispatches an action
- **`subscribe()`** — adds a change listener to state
- **`unsubscribe()`** — stops calling your listener method when state changes

### Actions
**Actions are plain JavaScript objects that represent events or intentions to modify the state.** They have a **`type`** property that describes the action and can also include additional data. Actions are dispatched to the store using the `store.dispatch()` method.

An action is sent or dispatched from the view. Actions are payloads that can be read by Reducers. An action is a pure object created to store the information about a user's event. It includes information such as the type of action, time of occurrence, location of occurrence, its coordinates, and which state it aims to change.

### Reducers
**Reducers are pure functions that specify how the state should change in response to actions.** They take the **current state** and an **action** as arguments and return a **new state**. Reducers define how the state is transformed and updated.

A reducer reads the payload from the action and then updates the store via the state accordingly. It is a pure function that returns a new state from the initial state.

> **Why are Redux state functions called reducers?** Because they are used to **reduce** the current state and an action into the next state. The reducer takes the current state and an action as input and returns the next state.

### Dispatch
**Dispatching an action is the process of sending an action to the store.** Components can dispatch actions using the `dispatch()` method provided by the Redux store.

### Connect
**The `connect()` function is used to connect components to the Redux store.** It allows components to access the state and dispatch actions.

---

## 18.6 Using Redux — step by step

### Step 1 — Install the dependencies
```bash
npm install redux react-redux
```

### Step 2 — Create the Redux store
Use `createStore()` from the Redux library. The store holds the application state and provides methods to dispatch actions and subscribe to changes.

```jsx
import { createStore } from 'redux';
import rootReducer from './reducers';

const store = createStore(rootReducer);
```
Here, `rootReducer` represents the combined reducers of your application. Reducers are functions that handle state updates based on dispatched actions.

### Step 3 — Wrap the application with a `<Provider>`
The `<Provider>` component from React Redux should wrap your application, providing the Redux store to all components that need access to the state.

```jsx
import { Provider } from 'react-redux';

ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('root')
);
```

### Step 4 — Connect components to the Redux store
To access the Redux state and dispatch actions, connect your components to the store using the `connect()` function or React hooks provided by `react-redux`.

```jsx
import { connect } from 'react-redux';

function MyComponent({ data, dispatch }) {
  // Access data from the Redux state

  const handleClick = () => {
    // Dispatch an action
    dispatch({ type: 'INCREMENT' });
  };

  return (
    <div>
      <p>Data: {data}</p>
      <button onClick={handleClick}>Increment</button>
    </div>
  );
}

const mapStateToProps = (state) => {
  return {
    data: state.data,
  };
};

export default connect(mapStateToProps)(MyComponent);
```

---

## 18.7 Redux middleware

### Redux Thunk
**Redux Thunk is a middleware that allows you to write action creators that return a function instead of an action.** This function can then be used to perform async logic and dispatch other actions.

### redux-saga
**redux-saga is a library that allows you to handle side effects in a Redux application by using generator functions.** It provides a way to handle async actions and to separate the logic for handling side effects from the rest of the application.

---

## 18.8 Redux vs Context API — when to use which

**React Context** is a built-in feature of React that allows you to share data between components without having to pass props down through multiple levels of the component tree.

**React Redux** is a library that allows you to connect your React components to a Redux store. It provides a way to access the state from the store and to dispatch actions to modify the state.

### Downsides of Redux compared to Flux
- The learning curve is steeper as it has a lot more concepts
- It can create **unnecessary complexity for small or simple applications**
- It can make debugging more difficult because the state is not visible in the components
- It can lead to verbose and repetitive code because actions and action creators are separate files

> **Practical guidance:** for a small app, start with `useState` and lift state up. Reach for Context when you have genuine cross-cutting global state (theme, auth). Reach for Redux only when the app is big enough that a predictable, centrally-logged state machine earns its complexity.

---
---

# PART 19 — Performance Optimization

## 19.1 The golden rule

> **Don't optimize prematurely.**
>
> Memoization and virtualization add complexity and can even **hurt** performance if used blindly. **Profile first**, fix real bottlenecks, and prefer structural fixes (state placement, composition) over reflexive `memo()`.
>
> **Measure before you memoize.**

---

## 19.2 The 12 key optimization techniques

### 01 — Image Optimization
Optimizing images can significantly reduce the load time of your application.

**Implementation:**
- Use modern image formats (e.g. **WebP**) and tools for compressing images.
- Serve **appropriately sized** images based on the user's device.

*(Recall: media — images — is what takes the longest to load on most websites.)*

---

### 02 — Route-Based Lazy Loading
Load routes and their associated components only when they are needed, reducing the initial load time.

**Implementation:** use React Router's `lazy` and `Suspense` for route-based code splitting.
```jsx
import React, { Suspense, lazy } from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

const Home = lazy(() => import('./Home'));
const About = lazy(() => import('./About'));

function App() {
  return (
    <Router>
      <Suspense fallback={<div>Loading...</div>}>
        <Switch>
          <Route path="/" exact component={Home} />
          <Route path="/about" component={About} />
        </Switch>
      </Suspense>
    </Router>
  );
}
```

---

### 03 — Component Lazy Loading
Load components only when they are needed to reduce the initial load time.
```jsx
import React, { Suspense, lazy } from 'react';

const LazyComponent = lazy(() => import('./LazyComponent'));

function App() {
  return (
    <div>
      <Suspense fallback={<div>Loading...</div>}>
        <LazyComponent />
      </Suspense>
    </div>
  );
}
```

---

### 04 — `useMemo`
Memoize expensive calculations to avoid recalculating them on every render.
```jsx
import React, { useMemo } from 'react';

function ExpensiveComponent({ data }) {
  const processedData = useMemo(() => {
    // expensive computation
    return processData(data);
  }, [data]);

  return <div>{processedData}</div>;
}
```

**When should you use `useMemo`?** Only for **genuinely expensive computations that measurably affect render time** — not for trivial arithmetic.

> ⚠️ **Overusing `useMemo`:**
>
> | ❌ DON'T | ✅ DO |
> |---|---|
> | `useMemo(() => a + b, [a,b])` | `const sum = a + b;` — too cheap to memoize |

---

### 05 — `React.memo`
Prevent unnecessary re-renders of functional components by memoizing them.
```jsx
const MyComponent = memo(function MyComponent({ prop1, prop2 }) {
  // component logic
});
```

**React.memo** is a higher-order component that allows you to optimize the performance of functional components by memoizing the component's output. **It prevents the component from re-rendering when its props haven't changed.** It skips the re-render if props are **shallow-equal**.

```jsx
const Row = memo(function Row(props) {
  return <li>{props.label}</li>;
});
```

> ⚠️ **Wrapping every component in `memo()` is a top performance mistake.** Use it deliberately.

---

### 06 — `useCallback`
Memoize functions to prevent them from being re-created on every render.
```jsx
import React, { useCallback } from 'react';

function MyComponent({ onClick }) {
  const handleClick = useCallback(() => {
    // handle click
  }, [onClick]);

  return <button onClick={handleClick}>Click me</button>;
}
```

**When should you use `useCallback`?** When a function identity is **passed to a memoized child** or used as an **effect dependency**. `useCallback` pairs with `memo()` to keep child props stable.

> ⚠️ **Overusing `useCallback`:**
>
> | ❌ DON'T | ✅ DO |
> |---|---|
> | `useCallback(() => {}, [])` when no children use it | Only wrap functions passed to memoized children |

---

### 07 — `useEffect` Cleanup
Clean up side effects in `useEffect` to avoid memory leaks and ensure proper resource management.
```jsx
import React, { useEffect } from 'react';

function MyComponent() {
  useEffect(() => {
    const handleScroll = () => {
      // handle scroll
    };

    window.addEventListener('scroll', handleScroll);

    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, []);

  return <div>Scroll to see effect</div>;
}
```

---

### 08 — Throttling and Debouncing
Throttle or debounce expensive operations (e.g. API calls, event handlers) to improve performance.

**Implementation:** use lodash's `throttle` and `debounce` functions.
```jsx
import { throttle, debounce } from 'lodash';

const handleScroll = throttle(() => {
  // handle scroll
}, 1000);

const handleSearch = debounce((query) => {
  // handle search
}, 500);

window.addEventListener('scroll', handleScroll);
inputElement.addEventListener('input', (e) => handleSearch(e.target.value));
```

---

### 09 — Fragments
Use fragments to avoid unnecessary wrapper elements in the DOM, which can reduce the number of nodes and improve rendering performance.
```jsx
import React from 'react';

function MyComponent() {
  return (
    <>
      <div>First element</div>
      <div>Second element</div>
    </>
  );
}
```

---

### 10 — `useTransition`
Use `useTransition` to handle state transitions **without blocking the UI**, improving the perceived performance.
```jsx
import React, { useState, useTransition } from 'react';

function MyComponent() {
  const [isPending, startTransition] = useTransition();
  const [count, setCount] = useState(0);

  const handleClick = () => {
    startTransition(() => {
      setCount(count + 1);
    });
  };

  return (
    <div>
      <button onClick={handleClick}>Increment</button>
      {isPending ? <div>Loading...</div> : <div>Count: {count}</div>}
    </div>
  );
}
```

---

### 11 — Web Workers
Use web workers to offload heavy computations to a **background thread**, keeping the UI responsive.

**worker.js**
```js
onmessage = function(e) {
  const result = heavyComputation(e.data);
  postMessage(result);
};
```

**Main component**
```jsx
import React, { useEffect } from 'react';

function MyComponent() {
  useEffect(() => {
    const worker = new Worker('./worker.js');

    worker.postMessage('some data');

    worker.onmessage = function(e) {
      console.log('Result from worker:', e.data);
    };

    return () => {
      worker.terminate();
    };
  }, []);

  return <div>Web Workers Example</div>;
}
```

---

### 12 — Caching with React Query
**React Query** helps in fetching, caching, and synchronizing server state in your React applications, **reducing network requests** and improving performance.

```jsx
import { persistQueryClient } from '@tanstack/react-query-persist-client';
import { createSyncStoragePersister } from '@tanstack/query-sync-storage-persister';

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      cacheTime: 1000 * 60 * 60 * 24, // 24 hours
    },
  },
});

const localStoragePersister = createSyncStoragePersister({
  storage: window.localStorage,
});
// const sessionStoragePersister = createSyncStoragePersister({ storage: window.sessionStorage })

persistQueryClient({
  queryClient,
  persister: localStoragePersister,
});
```

---

## 19.3 Virtualization

**Implement virtualization techniques for large lists or tables to render only the visible portion of the content**, rather than rendering the entire list.

Libraries like **`react-virtualized`** and **`react-window`** can help with virtualizing large data sets.

> **Large unvirtualized lists are a top performance killer.** Use stable keys and virtualize for 1000+ rows.

---

## 19.4 Performance profiling

Use tools like the **React Profiler**, **React DevTools**, or **browser DevTools** to identify performance bottlenecks in the application. Measure and optimize components or operations that cause performance issues, such as **excessive re-renders or inefficient data fetching**.

```jsx
<Profiler id="App" onRender={logRender}>
  <App />
</Profiler>
```

**Measure before optimizing — don't guess.**

---

## 19.5 State placement

- **Keep state as local as possible;** lift only when shared.
- **Move fast-changing state into the smallest component that needs it.** This prevents parent trees from re-rendering unnecessarily.
- **Global state re-renders everything subscribed to it.**

---

## 19.6 The common performance mistakes (checklist)

- ❌ Wrapping every component in `memo()`
- ❌ Memoizing cheap calculations
- ❌ Creating new objects/arrays inline as props (in hot render paths)
- ❌ Storing derived data in state instead of computing it
- ❌ Skipping the Profiler and guessing
- ❌ Using arrow functions in render methods *(they create a new function on every render, which can negatively impact performance and cause children to re-render even when props haven't changed)*
- ❌ Large unvirtualized lists
- ❌ Using array indexes as keys in reorderable lists

---
---

# PART 20 — Testing

## 20.1 Why test?

Testing is an essential part of the software development process, and React provides several testing frameworks and libraries widely used in the React ecosystem.

**These frameworks help ensure that React components and features are working as expected and that any changes to the codebase do not introduce regressions.**

---

## 20.2 The two main tools

### Jest
**Jest is a popular JavaScript testing framework** widely used for testing utilities including **assertions, test runners, and mocking capabilities**. Jest is known for its **simplicity, speed and ease of use**. It supports both **unit testing and integration testing** of React components and provides seamless integration with React through the **`react-test-renderer`** package.

### React Testing Library
**React Testing Library is a testing utility that encourages testing components from the user's perspective.** It provides a simple and intuitive API for querying and interacting with React components in a way that closely mimics how users would interact with the actual application.

**React Testing Library promotes testing the behaviour and output of components rather than their implementation details**, resulting in more robust and maintainable tests.

---

## 20.3 Writing a unit test for a component

When writing unit tests for React components, we typically test the **rendering, behaviour and state changes** of the component.

```jsx
import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import MyComponent from './MyComponent';

test('renders correctly and handles click event', () => {
  const { getByText } = render(<MyComponent />);

  // Test initial rendering
  expect(getByText('Initial Text')).toBeInTheDocument();

  // Test click event
  const button = getByText('Click me');
  fireEvent.click(button);
  expect(getByText('Updated Text')).toBeInTheDocument();
});
```

**How this works:**
- The **`render()`** function from `@testing-library/react` renders the component and provides querying methods like **`getByText`** to access and interact with the rendered component.
- Assertions are made using the **`expect()`** function to verify the expected behaviour and output.
- **`fireEvent`** simulates user interactions.

---

## 20.4 Testing hooks and asynchronous operations

Testing React hooks and asynchronous operations can be handled using **Jest's asynchronous test capabilities and mock functions**.

For testing asynchronous code, we need to use **`async/await`** or the **`done`** callback to handle the asynchronous nature of the operations. Jest provides utilities like **`waitFor`** to wait for specific conditions in the component before making assertions.

```jsx
import React from 'react';
import { render, waitFor } from '@testing-library/react';
import { act } from 'react-dom/test-utils';
import { useDataFetch } from './useDataFetch';
import MyComponent from './MyComponent';

jest.mock('./useDataFetch');   // Mock the data fetching hook

test('renders component with fetched data', async () => {
  useDataFetch.mockReturnValue({
    data: 'Mocked Data',
    loading: false,
    error: null,
  });

  await act(async () => {
    const { getByText } = render(<MyComponent />);
    await waitFor(() =>
      expect(getByText('Mocked Data')).toBeInTheDocument()
    );
  });
});
```

**How this works:**
- The `useDataFetch` hook is **mocked** using `jest.mock()` to simulate the data-fetching behaviour.
- The test uses **`act()`** from `react-dom/test-utils` to wrap the asynchronous code.
- **`waitFor()`** from `@testing-library/react` waits for the expected condition before making assertions.

> **By combining Jest's testing capabilities with React Testing Library, we can effectively write unit tests for React components, test React hooks, and handle asynchronous operations, ensuring reliability.**

---
---

# PART 21 — Best Practices, Debugging and Common Mistakes

## 21.1 Best practices for organising and structuring React code

### Component Organization
Organise components into **logical and reusable units**. Use a component-based architecture, where **each component has a single responsibility** and can be easily reused in different parts of the application.

### File Structure
Follow a **consistent file structure** to keep the codebase organized. Consider grouping related files together — such as components, styles and tests — to improve maintainability and ease of navigation.

> **Note:** React doesn't have opinions on how you put files into folders. Some developers group their files by **feature**. When moving files into folders, remember to **export** them so you can import them where necessary.

### Container and Presentational Components
Implement the **container-presentational component pattern**:
- **Container components** are responsible for managing state, handling data, fetching, and interacting with the Redux store.
- **Presentational components** focus on rendering UI elements and receiving props to display data.

### Separate concerns
Keep concerns separated between components. **Separate rendering logic from business logic**, and avoid mixing presentational code and state-management code in the same component.

### Use React hooks
Utilize React hooks such as `useState`, `useEffect` and `useContext` to manage component state, handle side effects and share state across components. **Hooks provide a more concise and readable way to write functional components.**

### Maintain Readability
Write clean, readable code by:
- Following **naming conventions**
- Using **descriptive variable and function names**
- **Commenting** when necessary
- **Breaking down complex components** into smaller, more manageable functions or components

### Config files
Create a **config file** (also called a **constants file**) in your project. Put all hardcoded values into it:

```js
// config.js
export const IMG_CDN_URL = "https://some-cdn-url/";
export const restaurantList = [ /* ... */ ];
```
Then import where needed:
```jsx
import { IMG_CDN_URL } from "./config";
```

---

## 21.2 Module exports and imports

There are **2 ways of exporting**:

### (i) Default export
- This is the **default** way.
- It means you want to export **only one** value.
- **There can be only one default export per module.**

```jsx
const Header = () => { /* ... */ };
export default Header;
```
```jsx
import Header from "./components/Header";
```
The imported name is given **locally** to the variable and **doesn't have to match** the original export name.

### (ii) Named exports
```jsx
export const Title = () => { /* ... */ };
```
```jsx
import { Title } from "./components/Header";
```
Named exports **must** match the exported name (unless aliased).

### Both together
| Header.js | App.js |
|---|---|
| `export const Title = () => {..}`<br>`const Header = () => {..}`<br>`export default Header` | `import Header, { Title } from "./components/Header";` |

### Importing everything
```jsx
import * as Obj from "./components/Header";
// then use Obj.Title, Obj.Header
```

> **When you are using a component in the same file, you don't have to export it at all.**

> A **module** is a self-contained unit that can expose assets to other modules using `export`, and acquire assets from other modules using `import`.

---

## 21.3 Debugging and troubleshooting common issues

### 1. Use developer tools
Leverage the browser's developer tools — such as the **JavaScript console** and **React DevTools** — to debug and inspect your React application. **These tools provide insights into component hierarchies, state changes, and potential errors.**

### 2. Debugging techniques
Implement **console logging** or use the **`debugger`** statement to examine variable values, track a component's lifecycle, or identify unexpected behaviour. This can help pinpoint the source of issues.

### 3. Error handling
Implement proper error handling techniques such as:
- **`try...catch` blocks**
- **Error boundaries**
- **Global error handling components** like `componentDidCatch`

This ensures that errors are **caught and gracefully handled**, preventing application crashes or unexpected behaviour.

### 4. Testing and linting
Write **unit tests** for React components and use **linting tools like ESLint** to catch common coding errors and enforce best practices. **Testing and linting can help identify issues early in the development process and improve code quality.**

---

## 21.4 Error boundaries

**Error boundaries are React components that catch JavaScript errors anywhere in their child component tree, log those errors, and display a fallback UI.**

They were introduced in **React v16** and they allow you to handle errors gracefully and ensure that your application continues to function even if there is an error.

### Error boundaries vs try/catch

| try/catch block | Error boundary |
|---|---|
| Works with **imperative** code | Meant for **declarative** code to render on the screen |
| A **language-level construct** that lets you handle exceptions occurring during the execution of the code inside the block | A **React component** that catches JS errors anywhere in its child component tree, logs them, and displays a fallback UI |
| Used to handle exceptions in JavaScript | Used specifically to handle errors in a React application |

```jsx
<ErrorBoundary fallback={<Oops />}>
  <Widget />
</ErrorBoundary>
```

---

## 21.5 Strict Mode

**Strict mode is a development-only feature in React that highlights potential problems in an application.** When a component is rendered in strict mode, React runs **extra checks and warnings** for any potential issues. This helps you identify and fix problems before they become bigger issues.

---

## 21.6 The eleven common mistakes — DON'T / DO table

| Mistake | ❌ DON'T | ✅ DO |
|---|---|---|
| **Missing Keys** | `list.map(i => <Row {...i} />)` | `list.map(i => <Row key={i.id} {...i} />)` |
| **Bad Controlled/Uncontrolled** | `<input value={v} />` — no onChange | `<input value={v} onChange={onChange} />` |
| **Wrong useEffect Deps** | `useEffect(() => { load(id); }, [])` | `useEffect(() => { load(id); }, [id])` |
| **State Sync Problems** | `useEffect(() => setLocal(prop), [prop])` | Derive during render, or lift state up |
| **Unnecessary useEffect** | `useEffect(() => setFull(a+b), [a,b])` | `const full = a + b;` — just compute it |
| **Prop Drilling** | Passing props through 4+ layers unused | Use Context or component composition |
| **Mutating State Directly** | `state.items.push(x); setState(state)` | `setState({ ...state, items: [...state.items, x] })` |
| **Incorrect Async Handling** | `async function` as the useEffect fn directly | `useEffect(() => { (async()=>{...})(); }, [])` |
| **Overusing useMemo** | `useMemo(() => a + b, [a,b])` | `const sum = a + b;` — too cheap to memoize |
| **Server/Client Boundary** | Using `useState` inside a Server Component | Add `'use client'` or move state down |
| **Overusing useCallback** | `useCallback(() => {}, [])` when no children use it | Only wrap fns passed to memoized children |

---

## 21.7 The Golden Rules

> **Derive, don't sync · keep state local · let Actions own async status · measure before you memoize · push data-fetching to the server when you can.**

### Best practices checklist
- Small components
- Compose over inherit
- Derive, don't sync
- Stable keys always
- Keep state local
- Push data-fetching to the server
- Profile first
- `memo()` sparingly

### Component pattern best practices

| Pattern | Best practice |
|---|---|
| **Functional Components** | Default in modern React — class components are legacy |
| **Props** | Treat props as read-only; never mutate them |
| **Children** | Enables flexible composition without prop explosion |
| **Conditional Rendering** | Avoid nested ternaries — extract to a variable or component |
| **Lists & Keys** | Never use array index as key if list can reorder |
| **Event Handling** | Avoid inline object/array literals in hot render paths |
| **Controlled Components** | React state is the single source of truth |
| **Uncontrolled Components** | Read via ref on submit; good for simple/perf-sensitive forms |
| **Composition** | Prefer composition over deep prop drilling or inheritance |
| **Custom Hooks** | Extract reusable stateful logic; prefix with `use` |

---
---

# PART 22 — Building a Real App: The "Food Villa" Walkthrough

*This part ties everything together. It follows the construction of a real food-ordering app from scratch.*

## 22.1 Plan before you code

> **"Whenever you are writing code, do planning."**

### The app wireframe

**App name: Food Villa**

```
┌────────────────────────────────────────────────┐
│  LOGO              Home  About  Support  Cart  │   ← Header / Nav bar
├────────────────────────────────────────────────┤
│  [ Search bar                          ]       │
│  ┌────────┐ ┌────────┐ ┌────────┐             │
│  │ Image  │ │ Image  │ │ Image  │             │
│  │ Name   │ │ Name   │ │ Name   │  ← Cards    │   ← Body
│  │Cuisines│ │Cuisines│ │Cuisines│             │
│  │ ★ 4.2  │ │ ★ 4.1  │ │ ★ 4.5  │             │
│  └────────┘ └────────┘ └────────┘             │
├────────────────────────────────────────────────┤
│  links          @2022 FoodVilla Copyright      │   ← Footer
└────────────────────────────────────────────────┘
```

### The component tree
```jsx
const AppLayout = () => {
  return (
    // - Header
    //     - Logo
    //     - Nav Items (on right side)
    //     - Cart
    // - Body
    //     - Searchbar
    //     - Restaurant List
    //         - RestaurantCard
    //             - Image
    //             - Name
    //             - Rating
    //             - Cuisines
    // - Footer
    //     - links
    //     - Copyrights
  );
};
```

> Remember: Is JSX mandatory? **No.** Is TypeScript mandatory? **No.** Is ES6 mandatory? **No.** They are all just tools that make life easier.

---

## 22.2 Building the Header

```jsx
const Title = () => {
  return (
    <a href="/">
      <img
        alt="food_villa_logo"
        src="https://some-url/logo.png"
      />
    </a>
  );
};

const HeaderComponent = () => {
  return (
    <div className="header">
      <Title />
      <div className="nav-items">
        <ul>
          <li>Home</li>
          <li>About</li>
          <li>Contact</li>
          <li>Cart</li>
        </ul>
      </div>
    </div>
  );
};
```

---

## 22.3 Building the RestaurantCard — from hardcoded to dynamic

### Step 1 — Hardcoded
```jsx
const RestaurantCard = () => {
  return (
    <div className="card">
      <img src="https://some-url/image.jpg" />
      <h2>Burger King</h2>
      <h3>Burgers, American</h3>
      <h4>4.2 stars</h4>
    </div>
  );
};
```
**Problem:** the name, image and other data won't always be the same. It should be dynamic.

### Step 2 — Using a JavaScript object
```jsx
const burgerKing = {
  name: "Burger King",
  image: "https://some-url/image.jpg",
  cuisines: ["Burger", "American"],
  rating: "4.2",
};

const RestaurantCard = () => {
  return (
    <div className="card">
      <img src={burgerKing.image} />
      <h2>{burgerKing.name}</h2>
      <h3>{burgerKing.cuisines.join(", ")}</h3>
      <h4>{burgerKing.rating}</h4>
    </div>
  );
};
```
**Problem:** in the real world, data doesn't come as a single object. It comes as an **array of objects**.

### Step 3 — Passing props
```jsx
const RestaurantCard = (props) => {
  return (
    <div className="card">
      <img src={IMG_CDN_URL + props.restaurant.data?.cloudinaryImageId} />
      <h2>{props.restaurant.data?.name}</h2>
      <h3>{props.restaurant.data?.cuisines.join(", ")}</h3>
      <h4>{props.restaurant.data?.deliveryTime} minutes</h4>
    </div>
  );
};

const Body = () => {
  return (
    <div className="restaurant-list">
      <RestaurantCard restaurant={restaurantList[0]} />
      <RestaurantCard restaurant={restaurantList[1]} />
      <RestaurantCard restaurant={restaurantList[2]} />
    </div>
  );
};
```

### Step 4 — Destructuring
```jsx
const RestaurantCard = ({ name, cuisines, cloudinaryImageId, deliveryTime }) => {
  return (
    <div className="card">
      <img src={IMG_CDN_URL + cloudinaryImageId} />
      <h2>{name}</h2>
      <h3>{cuisines.join(", ")}</h3>
      <h4>{deliveryTime} minutes</h4>
    </div>
  );
};
```

### Step 5 — Spread operator
```jsx
const Body = () => {
  return (
    <div className="restaurant-list">
      <RestaurantCard {...restaurantList[0].data} />
      <RestaurantCard {...restaurantList[1].data} />
      <RestaurantCard {...restaurantList[2].data} />
    </div>
  );
};
```
**Problem:** if you have 100 restaurants, writing this out is not viable.

### Step 6 — `.map()` — the final form
```jsx
const Body = () => {
  return (
    <div className="restaurant-list">
      {restaurantList.map((restaurant) => {
        return (
          <RestaurantCard
            {...restaurant.data}
            key={restaurant.data.id}
          />
        );
      })}
    </div>
  );
};
```

**Reading the code:** `restaurantList.map(...)` maps over the array, passing a **callback function**. This callback takes each object — `(restaurant)` — and for each object in the array, returns a piece of JSX (the `<RestaurantCard/>`). We spread the `restaurant` object into the card and give it a `key`.

---

## 22.4 Config-Driven UI

**All of the UI (say, the Swiggy home page) is driven by a config which is sent by the backend (the API).**

### Why?
Swiggy should work in Kolkata, Dehradun, Delhi and whatever location — and we should show different website information for each location. To do that, we control our front-end using a **config**. This is why it is known as **Config Driven UI**. **All of it is controlled by the backend.**

### How the config is shaped
Suppose the UI has a logo and nav at the top, a **carousel** of offer cards (50% OFF, DELIVERY FREE, DIWALI OFFER, 20% OFF), then "590 restaurants" and the restaurant grid.

The config coming from the backend would look like:
```js
const config = [
  {
    type: "carousel",              // These offers differ by location
    cards: [
      { offerName: "50% OFF" },
      { offerName: "No Delivery Charge" }
    ]
    // If there are no offers for a location, the backend
    // simply doesn't send this object, or sends empty cards.
  },
  {
    type: "restaurants",
    cards: [
      {
        name: "Burger King",
        image: "https://some-url",
        cuisines: ["Burger", "American"],
        rating: "4.2",
      },
      {
        name: "KFC",
        image: "https://some-url",
        cuisines: ["Burger", "American"],
        rating: "4.2",
      }
    ]
  }
];
```

**Only the backend changes the offers, and the website renders accordingly.**

> **Everything that we build is a Config Driven UI.**

---

## 22.5 Building the search functionality

### The complete implementation

```jsx
import { useState, useEffect } from "react";

function filterData(searchTxt, restaurants) {
  return restaurants.filter((restaurant) =>
    restaurant.data.name.toLowerCase().includes(searchTxt.toLowerCase())
  );
}

const Body = () => {
  const [searchTxt, setSearchTxt] = useState("");
  const [allRestaurants, setAllRestaurants] = useState([]);
  const [filteredRestaurants, setFilteredRestaurants] = useState([]);

  useEffect(() => {
    getRestaurants();
  }, []);

  async function getRestaurants() {
    const data = await fetch("https://some-api-url");
    const json = await data.json();
    setAllRestaurants(json?.data?.cards[2]?.data?.data?.cards);
    setFilteredRestaurants(json?.data?.cards[2]?.data?.data?.cards);
  }

  // Early return / conditional rendering
  if (!allRestaurants) return null;

  return allRestaurants?.length === 0 ? (
    <Shimmer />
  ) : (
    <>
      <div className="search-container">
        <input
          type="text"
          className="search-input"
          placeholder="Search"
          value={searchTxt}
          onChange={(e) => setSearchTxt(e.target.value)}
        />
        <button
          className="search-btn"
          onClick={() => {
            const data = filterData(searchTxt, allRestaurants);
            setFilteredRestaurants(data);
          }}
        >
          Search
        </button>
      </div>

      {filteredRestaurants?.length === 0 ? (
        <h1>No matches found</h1>
      ) : (
        <div className="restaurant-list">
          {filteredRestaurants.map((restaurant) => (
            <RestaurantCard
              {...restaurant.data}
              key={restaurant.data.id}
            />
          ))}
        </div>
      )}
    </>
  );
};
```

### The bug you will hit — and why you need TWO state variables

**The bug:** after one search, the state gets updated. Then when you search again, it doesn't work.

**The cause:** `restaurants` gets filtered *down*. The next search then filters the already-filtered list.

**The fix:** you should never overwrite the master list. **Maintain 2 variables:**
- **Var 1** ⇒ the list of **all** restaurants
- **Var 2** ⇒ the list of **filtered** restaurants

```jsx
const [allRestaurants, setAllRestaurants] = useState([]);
const [filteredRestaurants, setFilteredRestaurants] = useState([]);
```

Whenever you filter, you **filter from `allRestaurants`**. You **display `filteredRestaurants`** in the UI. On the first API call, set both to the same data.

### Homework from the course
1. Check for `allRestaurants` and show the Shimmer.
2. Then check whether `filteredRestaurants` exists or not.
3. You should see "No matches" **only** when `filteredRestaurants.length` is zero.

Also worth exploring: case-insensitive conversion in the search, and a Login/Logout toggle button.

---

## 22.6 Storing images

To store images locally, **create a folder called `assets`** and keep images inside it.

But remember: **CDN is a great place to host images** — it's faster, it caches, it has ~100% uptime, and the images are already optimized.

---
---

# PART 23 — React 19: The Modern APIs

*Once you have the fundamentals from Parts 1–22, this is what modern React adds.*

## 23.1 React 19 overview

React 19 refines the mental model introduced by **Concurrent Rendering**: **less imperative state-syncing, more declarative async.**

The headline additions — **Actions, `use()`, and native form integration** — remove the boilerplate that used to surround loading states, pending UI, and optimistic updates.

**Server Components** and **Server Functions** push data-fetching and mutations onto the server by default, shrinking client bundles without leaving the component model.

### What is React 19?
A major release focused on **simplifying async UI, forms, and the client/server boundary** while keeping the component model you already know.

### Key improvements
Fewer hooks needed for common async work, native form handling, faster hydration, and first-class metadata & resource loading.

### The full feature list

| Feature | What it does |
|---|---|
| **Server Components** | Components that render on the server, ship **zero JS** to the client, and can read data directly — no client-side fetch waterfall. |
| **Actions** | Async functions passed to forms, transitions, or event handlers. **React manages pending, error, and optimistic state for you.** |
| **New Form APIs** | `<form action={fn}>` now accepts async functions directly — no manual `preventDefault`, fetch, or state wiring. |
| **`use()` API** | Reads the value of a Promise or Context **during render** — works conditionally, unlike other hooks. |
| **ref as a Prop** | Function components can accept `ref` directly as a prop — **`forwardRef` is no longer required**. |
| **Improved Hydration** | Better mismatch diagnostics and more resilient hydration that recovers gracefully from third-party DOM edits. |
| **Metadata Support** | `<title>`, `<meta>`, and `<link>` can be rendered **anywhere in the tree** — React hoists them into `<head>` automatically. |
| **Stylesheet Support** | `<link rel="stylesheet">` with precedence hints lets React control load order and dedupe styles across the tree. |
| **Preloading APIs** | `preload`, `preinit`, `prefetchDNS` and `preconnect` (from `react-dom`) give components fine-grained control over resource loading. |
| **Error Handling** | `onCaughtError` / `onUncaughtError` root options plus clearer error boundaries reduce noisy duplicate logging. |

---

## 23.2 The new React 19 APIs and hooks

### `use()`
Reads a **Promise or Context value during render**.
```jsx
const data = use(promise);
const theme = use(ThemeContext);
```
> **Can be called conditionally — unlike other hooks.** The Promise must stay stable across renders.

### `useActionState()`
Tracks **pending / result / error** state for an Action.
```jsx
const [state, formAction, pending] = useActionState(updateName, null);
```
> Use for any form or button that calls an async function. Returns `[state, dispatchAction, pending]`.

### `useOptimistic()`
Shows **instant optimistic UI** while an Action is in flight.
```jsx
const [opt, addOpt] = useOptimistic(
  list,
  (s, item) => [...s, item]
);
```
> **Automatically reverts if the underlying Action throws.**

### `useFormStatus()`
Reads the **pending status of a parent `<form>`**.
```jsx
function Btn() {
  const { pending } = useFormStatus();
  return <button disabled={pending} />;
}
```
> Must be called from a component rendered **inside** the form. No prop drilling required.

### Actions
An async function passed to a transition, form, or handler.
```jsx
startTransition(async () => {
  await saveData();
});
```
> React tracks **pending, error, and optimistic state** for you.

### Server Actions / Functions
An async function marked `"use server"` runs **only on the server**.
```jsx
async function createPost(fd) {
  'use server';
  await db.posts.create(fd);
}
```
> Requires a framework with server support (e.g. **Next.js**).

### ref as a Prop
```jsx
function Input({ ref, ...props }) {
  return <input ref={ref} {...props} />;
}
```
> `forwardRef` still works, but is **no longer required**.

---

## 23.3 Forms in React 19 — before and after

This is the single clearest demonstration of what React 19 changed.

### The traditional pattern (React 18)
```jsx
function Form() {
  const [pending, setPending] = useState(false);
  const [error, setError] = useState(null);

  async function handleSubmit(e) {
    e.preventDefault();
    setPending(true);
    try {
      await updateName(e.target.name.value);
    } catch (err) {
      setError(err.message);
    }
    setPending(false);
  }

  return (
    <form onSubmit={handleSubmit}>
      <input name="name" />
      <button disabled={pending}>Save</button>
    </form>
  );
}
```

### The React 19 pattern
```jsx
function Form() {
  const [error, formAction, pending] = useActionState(
    async (prev, fd) => {
      try {
        await updateName(fd.get('name'));
        return null;
      } catch (err) {
        return err.message;
      }
    },
    null
  );

  return (
    <form action={formAction}>
      <input name="name" />
      <button disabled={pending}>Save</button>
    </form>
  );
}
```

**All of the pending/error state wiring is gone.** React manages it.

### The four common form states

**Form submission**
```jsx
<form action={formAction}>
  <input name="email" />
  <button>Submit</button>
</form>
```

**Pending state**
```jsx
function Btn() {
  const { pending } = useFormStatus();
  return (
    <button disabled={pending}>
      {pending ? 'Saving…' : 'Save'}
    </button>
  );
}
```

**Validation error**
```jsx
const [error, action] = useActionState(async (_, fd) => {
  if (!fd.get('email')) return 'Required';
  return null;
}, null);
```

**Optimistic UI**
```jsx
const [items, addOpt] = useOptimistic(
  list,
  (s, item) => [...s, item]
);

addOpt(newItem);   // instant UI
```

---

## 23.4 Server and Client Components

### The comparison table

| Concept | Runs Where | Ships JS? | Can Use Hooks / State? | Typical Use |
|---|---|---|---|---|
| **Client-side Rendering** | Browser | Yes | Yes | Interactive widgets, forms |
| **Server Rendering (SSR)** | Server, then hydrates | Yes | Yes | Fast first paint + interactivity |
| **Server Components** | Server only | **No** | **No** (no `useState`/`useEffect`) | Data-heavy, static-ish UI |
| **Client Components** | Server (SSR) + Browser | Yes | Yes | Anything with interaction |

### The directives

**`"use client"`** — Marks a module boundary. Everything imported below runs as a **Client Component**.
```jsx
'use client';

export function Counter() {
  const [n, setN] = useState(0);
  // ...
}
```

**`"use server"`** — Marks a function as a **Server Function/Action** callable from the client.
```jsx
'use server';

export async function save(data) {
  await db.write(data);
}
```

### Async components
Server Components may be **async functions** and `await` data directly in the component body.
```jsx
async function Page() {
  const posts = await getPosts();
  return <List items={posts} />;
}
```

### `use()` with Promises
In Client Components, `use()` **unwraps a Promise** passed down from a Server Component.
```jsx
function Comments({ promise }) {
  const data = use(promise);
  return <List items={data} />;
}
```

### Loading & error states
Wrap async Server Components in `<Suspense fallback={<Spinner />}>` for loading UI, and an **error boundary** (or a route-level `error.js` in frameworks) to catch rejected data fetches.

---

## 23.5 Server Side Rendering (SSR)

**To implement Server Side Rendering in a React application, you can use a library such as Next.js or `ReactDOMServer`.** These libraries allow you to render your React components on the **server** and send the resulting HTML to the browser.

This can improve the performance of your application by **reducing the initial load time** and providing a better experience for **search engines**.

### Next.js — major features
**NextJS is a framework for building web applications with React.** It provides a set of features for building server-rendered React applications:
- **Server-side rendering (SSR)** out of the box
- **Automatic code splitting** for faster load times
- Built-in **development server with hot reloading**
- Easy setup for custom routes with **file-system based routing**
- **Static site generation (SSG)**

---

## 23.6 The React 19 Decision Guide

**"Which hook or API do I need?"** — Start with the question closest to your problem. **Most rendering bugs trace back to picking the wrong tool here — especially reaching for `useEffect` when a derived value or an Action would do.**

| Question | Answer |
|---|---|
| Need local state? | → `useState` / `useReducer` |
| Need a side effect after render? | → `useEffect` |
| Need a mutable value with no re-render? | → `useRef` |
| Need state shared across components? | → Context, or an external store |
| Need to read an async resource? | → `use()` |
| Need form pending/result state? | → `useActionState()` |
| Need instant optimistic UI? | → `useOptimistic()` |
| Need a form's pending status in a child? | → `useFormStatus()` |
| Need to reduce bundle size? | → Server Components / `lazy()` |
| Need a performance optimization? | → **Profile first** → memoize only if proven |

---
---

# PART 24 — Quick Reference

## 24.1 React 19 syntax quick reference

**Component**
```jsx
function App() {
  return <div>Hi</div>;
}
```

**Props**
```jsx
function C({ a, b }) { /* ... */ }
<C a={1} b={2} />
```

**State**
```jsx
const [v, setV] = useState(0);
```

**Effect**
```jsx
useEffect(() => {
  // side effect
  return () => {};
}, [deps]);
```

**Context**
```jsx
const V = useContext(MyCtx);
```

**Reducer**
```jsx
const [s, d] = useReducer(fn, init);
```

**Custom Hook**
```jsx
function useThing() {
  const [v, setV] = useState();
  return v;
}
```

**Form Action**
```jsx
<form action={formAction}>
  ...
</form>
```

**Ref**
```jsx
const r = useRef(null);
<div ref={r} />
```

**Memoization**
```jsx
useMemo(() => calc(a), [a]);
useCallback(fn, [deps]);
```

**`use()`**
```jsx
const data = use(promiseOrCtx);
```

**`useActionState()`**
```jsx
const [s, action, pending] = useActionState(fn, initial);
```

**`useOptimistic()`**
```jsx
const [v, addOpt] = useOptimistic(state, reducer);
```

**`useFormStatus()`**
```jsx
const { pending } = useFormStatus();
```

**Suspense**
```jsx
<Suspense fallback={<Spinner />}>
  <Widget />
</Suspense>
```

**Error Boundary**
```jsx
<ErrorBoundary fallback={<Oops />}>
  <Widget />
</ErrorBoundary>
```

---

## 24.2 One-liner React snippets

Nine patterns worth memorizing.

**1. Conditional Rendering (Ternary)** — Renders Dashboard if the user is logged in, otherwise shows Login.
```jsx
{isLoggedIn ? <Dashboard /> : <Login />}
```

**2. Arrow Function with State Update** — Initializes a counter and defines an increment function in one line.
```jsx
const [count, setCount] = useState(0);
const increment = () => setCount(prev => prev + 1);
```

**3. Short-Circuit Conditional Render** — Renders a message only when `showMessage` is true.
```jsx
{showMessage && <p>Hello, User!</p>}
```

**4. Map Through Array to Render List** — Dynamically creates a list from an array of items.
```jsx
{items.map(item => <li key={item.id}>{item.name}</li>)}
```

**5. useEffect One-Liner (componentDidMount)** — Runs once when the component mounts.
```jsx
useEffect(() => console.log('Mounted'), []);
```

**6. Destructuring Props in a Functional Component** — Directly extracts `name` from props.
```jsx
const Welcome = ({ name }) => <h1>Hello, {name}</h1>;
```

**7. Default Prop with Destructuring** — Sets a default button label if none is passed.
```jsx
const Button = ({ label = "Click Me" }) => <button>{label}</button>;
```

**8. Dynamic Class Name** — Conditionally applies a CSS class based on state.
```jsx
<div className={`box ${isActive ? "active" : ""}`}></div>
```

**9. Inline Event Handler** — Triggers an alert on click without defining a separate function.
```jsx
<button onClick={() => alert("Clicked!")}>Click</button>
```

---

## 24.3 The complete hooks table

| Hook | Purpose | Watch out for |
|---|---|---|
| `useState` | Local component state | Updates are batched & async — don't read state right after setting it |
| `useEffect` | Sync with an external system after render | Missing/incorrect dependency array causes stale closures |
| `useContext` | Read a Context value without prop drilling | Re-renders on any context value change — split contexts |
| `useReducer` | State transitions via actions | Prefer over `useState` when next state depends on multiple sub-values |
| `useRef` | Mutable value that persists without re-rendering | Mutating `ref.current` does NOT trigger a re-render |
| `useMemo` | Memoize an expensive computed value | Not a guarantee — React may discard the cache |
| `useCallback` | Memoize a function identity across renders | Only useful with memoized children or effect deps |
| `useLayoutEffect` | Like `useEffect`, but synchronous before paint | Blocks the browser paint |
| `useImperativeHandle` | Customize the instance exposed via ref | Pairs with ref-as-prop in React 19 |
| `useDebugValue` | Label a custom hook's value in DevTools | Dev-only; zero production effect |
| `useId` | Stable unique ID for accessibility attrs | Do NOT use as a React key in a list |
| `useTransition` | Non-blocking state transitions | React 18+ |
| `useDeferredValue` | Show stale content while urgent content renders | React 18+; wraps a *value*, not an update |
| `useSyncExternalStore` | Subscribe to state living outside React | The tear-free way to read external stores |
| `useInsertionEffect` | Inject styles before layout is read | For CSS-in-JS libraries; not app code |
| `use()` | Read a Promise or Context during render | React 19; can be called conditionally |
| `useActionState()` | Track pending/result/error for an Action | React 19 |
| `useOptimistic()` | Instant optimistic UI | React 19; auto-reverts on error |
| `useFormStatus()` | Read parent form's pending status | React 19; must be inside the form |

---

## 24.4 Everything at a glance

**Core Hooks:** `useState` · `useEffect` · `useRef` · `useContext` · `useMemo` · `useLayoutEffect` · `useReducer` · `useCallback` · `useId`

**Concurrent & advanced hooks:** `useTransition` · `useDeferredValue` · `useSyncExternalStore` · `useInsertionEffect` · `useImperativeHandle` · `useDebugValue`

**Form APIs:** `useActionState()` · `useFormStatus()` · Actions · `useOptimistic()` · `<form action>` · `'use client'` · Server Actions · `'use server'` · Pending state · Optimistic UI

**React 19 APIs:** `use()` · ref as prop

**Server / Client Concepts:** Server Components · Client Components · CSR · Streaming · Hydration · SSR

**Best Practices:** Small components · Compose over inherit · Derive, don't sync · Stable keys always · Keep state local

**Performance Tips:** `memo()` sparingly · Split by route · Virtualize long lists · Local state placement · Push data-fetching to server · Profile first

**Interview Keywords:** Reconciliation · Batching · Suspense boundary · Concurrent rendering · Optimistic update · Hydration mismatch

**Avoid These Pitfalls:** Missing keys · Wrong effect deps · Mutating state directly · Prop drilling · Overusing memoization · Client/server mix-ups

**Syntax Essentials:** JSX + props · Controlled inputs · Hooks at top level · `key` on list items · Named exports

---

## 24.5 Glossary

| Term | Meaning |
|---|---|
| **Babel** | A JavaScript compiler/transpiler. Converts JSX to `React.createElement()` and converts new JS into older JS. |
| **Bundler** | A tool that combines multiple JS files into a single file. Webpack, Parcel, Vite, rollup, browserify. |
| **CDN** | Content Delivery Network — a network of servers that delivers content to users. |
| **CORS** | Cross Origin Resource Sharing — an HTTP-header mechanism controlling which origins can load resources. |
| **Component composition** | Using a component inside another component. |
| **Config-driven UI** | A UI whose structure and content are driven by a config object sent from the backend. |
| **DOM** | Document Object Model. |
| **Emmet** | An editor feature designed to speed up writing and editing code by providing shortcuts that expand into full code blocks. |
| **ES6** | ECMAScript 6 — a version of JavaScript. |
| **Flux** | An application architecture from Facebook providing unidirectional data flow. |
| **HMR** | Hot Module Reloading — the bundler tracks file changes and reloads automatically. |
| **HOC** | Higher-Order Component — a function taking a component and returning a new component with extra functionality. |
| **JSX** | JavaScript XML — a syntax extension that lets you write HTML-like code in JavaScript. |
| **Lifting state up** | Moving state management from a child component to its parent so it can be shared. |
| **Monolith** | The old architecture where everything (API, UI, notifications) was one big project. |
| **npm** | The package manager that comes with Node.js. |
| **Optional chaining (`?.`)** | Access an object's properties without checking whether the object exists. (ES2020) |
| **Polyfill** | Older replacement code that makes new features work in older browsers. |
| **Props** | Properties — read-only data passed from parent to child. |
| **Pure component** | A component that only re-renders if its props or state have changed. |
| **Reconciliation** | The process React uses to determine the minimal set of DOM changes. |
| **React Fiber** | The reconciliation engine introduced in React 16, breaking rendering into async chunks. |
| **Shimmer UI** | A skeleton loading placeholder that resembles the real content. |
| **SPA** | Single Page Application. |
| **Spread operator (`...`)** | Expands an iterable where multiple elements are expected. |
| **SSR** | Server Side Rendering. |
| **State** | Internal, mutable data owned by a component. |
| **Synthetic events** | React's cross-browser wrapper around native browser events. |
| **Transitive dependency** | A dependency of one of your dependencies. |
| **Tree shaking** | Removing unused code from the bundle. |
| **Virtual DOM** | A lightweight in-memory representation of the actual DOM. |

---

## 24.6 A 22-day study plan

| Day | Topic | Practice task |
|---|---|---|
| 1 | Parts 1–2: what React is, setup | Run `npx create-react-app`, change the text on the page |
| 2 | Part 3: JSX | Build a static profile card in JSX |
| 3 | Part 4: Components | Split that card into Header/Body/Footer components |
| 4 | Part 5: Props | Render 5 cards from an array of objects using props |
| 5 | Part 6: State | Build a counter; build a show/hide toggle |
| 6–7 | Part 7: Hooks | Build a component that fetches and displays data with useState + useEffect |
| 8 | Part 8: Events | Add buttons that change state; pass arguments to handlers |
| 9 | Part 9: Conditional rendering, lists, keys | Build a filterable list |
| 10 | Part 10: Forms | Build a controlled login form with validation |
| 11 | Part 11: Styling | Style your app three ways: inline, CSS file, CSS module |
| 12 | Part 12: APIs | Fetch from a public API, add a Shimmer UI |
| 13 | Part 13: Routing | Add 3 pages with react-router-dom and a dynamic detail page |
| 14 | Part 14: Virtual DOM, reconciliation | No code — read and be able to explain it out loud |
| 15 | Part 15: Bundlers, npm | Build the same app with Parcel instead of CRA |
| 16 | Part 16: Class components | Convert one of your function components to a class, and back |
| 17 | Part 17: Refs, Fragments, Portals, HOC, Context | Build a modal with a Portal |
| 18 | Part 18: State management | Replace prop drilling with Context |
| 19 | Part 19: Performance | Profile your app; add React.memo where the Profiler says it helps |
| 20 | Part 20: Testing | Write 3 tests with Jest + React Testing Library |
| 21 | Part 21: Best practices | Refactor your app against the DON'T/DO table |
| 22+ | Parts 22–23 | Build the Food Villa app end to end; then explore React 19 Actions |

---

## 24.7 Where to go next

- **The official React documentation** — react.dev
- **Babel's documentation** — to understand the JSX transform
- **browserslist.dev** — to see browser support for your config
- **Watch:** map/filter/reduce; async & defer; CORS explained
- **Read about:** React Fiber; the difference between `map` and `forEach`; the difference between HTML and JSX
- **Libraries worth knowing:** Formik or React Hook Form (forms), React Query / TanStack Query (server state), react-window (virtualization), styled-components (styling), Redux Toolkit (state)

---

**End of notes.**

*Interview questions from these files are in **REACT-INTERVIEW-QUESTIONS.md**.*
