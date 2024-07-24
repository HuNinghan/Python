// Import React and Component from react
import React, { Component } from 'react';

// Define a new class component
class App extends Component {
  render() {
    return (
      <div>
        <h1>Hello, React!</h1>
      </div>
    );
  }
}

// Export the App component
export default App;

// Import the App component
import App from './App';

// Render the App component
ReactDOM.render(<App />, document.getElementById('root'));