import React, { Component } from 'react'
import { Button, Card, Menu, activeItem, Container, Image, Header, Segment, Grid, List, Divider, Icon } from 'semantic-ui-react'
import { BrowserRouter as Router, Route, Link, Switch } from 'react-router-dom'

import Dashboard from '../Dashboard/Dashboard.jsx'

import styles from './styles.scss'

//homepage component
//by pressing button "get started", you can go to the main page(dashboard) to manage time
//group members and group information are in the Container tag

class Home extends Component {
    render() {
        return(

            <div>

              <div className="titlePlusBgImg">
                <div className="contentCenter">
                  <p>MANAGE YOUR TIME</p>
                  <Link to = {'/dashboard'}>
                      <Button primary size='huge'>
                      Get Started
                      <Icon name='right arrow' />
                    </Button>
                  </Link>

                </div>
              </div>

            <Container>

            <Grid columns={3} relaxed style={{ paddingBottom: '5em', paddingTop: '5em', marginLeft:'5em', marginRight:'5em' }}>
              <Grid.Column>
                <Segment textAlign='center' basic>
                  <Icon color='grey' size='big' name='browser' />
                  <Header as='h3' style={{ fontSize: '1.8em'}}>ROGER HO</Header>
                </Segment>
              </Grid.Column>
              <Grid.Column>
                <Segment textAlign='center' basic>
                <Icon color='grey' size='big' name='browser' />

                  <Header as='h3' style={{ fontSize: '1.8em'}}>TEJVEER SINGH</Header>
                </Segment>
              </Grid.Column>
              <Grid.Column>
                <Segment textAlign='center' basic>
                <Icon color='grey' size='big' name='browser' />

                  <Header as='h3' style={{ fontSize: '1.8em'}}>YAN XU</Header>
                </Segment>
              </Grid.Column>


            </Grid>
            </Container>
            <Segment
                  inverted
                  vertical
                >
                  <Container textAlign='center'>
                    <Grid style={{ margin: '0em 0em 0em', padding: '0em 0em' }} divided inverted stackable>
                      <Grid.Row>
                        <Grid.Column width={4}>
                          <Header inverted as='h4' content='Member' />
                          <List link inverted>
                            <List.Item as='a' href="https://github.com/TeemosCode">Roger Ho</List.Item>
                            <List.Item as='a' href="https://www.linkedin.com/in/tejveer-singh-13505658/">Tejveer Singh</List.Item>
                            <List.Item as='a' href="https://www.linkedin.com/in/yan-xu-14a419154/">Yan Xu</List.Item>

                          </List>
                        </Grid.Column>
                        <Grid.Column width={4}>
                          <Header inverted as='h4' content='Contact us' />
                          <List link inverted>
                            <List.Item as='a' href="mailto:pingche2@illinois.edu">pingche2@illinois.edu</List.Item>
                            <List.Item as='a' href="mailto:ts8@illinois.edu">ts8@illinois.edu</List.Item>
                            <List.Item as='a' href="mailto:yanxu3@illinois.edu">yanxu3@illinois.edu</List.Item>

                          </List>
                        </Grid.Column>

                        <Grid.Column width={7}>
                          <Header inverted as='h4' content='About' />
                          <p>This is a group project of a course Progr Analytics & Data Process in UIUC. This website aims to help users simulate total time it takes to finish a project based on individual tasks inputs.</p>
                        </Grid.Column>
                      </Grid.Row>
                    </Grid>

                    <Divider inverted fitted section />
                    <p style={{ margin: '0em 0em 0em', padding: '0em 0em' }} align="center">©2017 Manage 24</p>

                  </Container>
                </Segment>
                <Switch>
                    <Route exact path="/dashboard" component={Dashboard}/>
                </Switch>
            </div>
        )
    }
}

export default Home
