import React from 'react';
import Authentication from './components/Authentication';
import Interaction from './components/Interaction';
import Administration from './components/Administration';
import Support from './components/Support';

function App() {
  return (
    <div>
      <h1>My Project</h1>
      <Authentication />
      <Interaction />
      <Administration />
      <Support />
    </div>
  );
}

export default App;
