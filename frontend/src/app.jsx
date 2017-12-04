import React from 'react';
import ReactDom from 'react-dom';
import { BrowserRouter as Router, Route, Link, Switch } from 'react-router-dom';
import { Button, Segment, Label, Menu, activeItem, Input} from 'semantic-ui-react';

import Home from './components/Home/Home.jsx';
import Dashboard from './components/Dashboard/Dashboard.jsx';

import styles from './styles/main.scss';

ReactDom.render(


      <Router>
        <div>
        <Menu fixed='top' size='massive'>
          <Link to = {'/'}>
            <Menu.Item name="Manage24" active={activeItem === "Manage24"}/>
          </Link>

          </Menu>

          <Switch>
              <Route exact path="/" component={Home}/>
              <Route exact path="/dashboard" component={Dashboard}/>
          </Switch>
          </div>
      </Router>,
    document.getElementById('react-app')
);
