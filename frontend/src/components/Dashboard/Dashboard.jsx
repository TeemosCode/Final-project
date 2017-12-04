import React, { Component } from 'react'
import { Button, Card, Menu, activeItem, Container, Image, Header, Segment, Grid, List, Divider, Icon, Input, Dropdown } from 'semantic-ui-react'
import { Link } from 'react-router-dom'
import axios from 'axios'

import styles from './styles.scss'
const options = [
  { key: 'Normal', text: 'Normal', value: 'Normal' },
  { key: 'uniform', text: 'uniform', value: 'uniform' },
  { key: 'PERT', text: 'PERT', value: 'PERT' },
]

class Dashboard extends Component {



    render() {


            return(
              <div className = "Dashboard">

                <div>
                <Grid columns={3} divided>
                 <Grid.Row>
                   <Grid.Column width = {3}>
                   </Grid.Column>
                   <Grid.Column width = {8}>
                     <List divided verticalAlign='middle'>
                        <List.Item>
                          <List.Content floated='right'>
                            <Icon name='zoom' />
                          </List.Content>

                          <Image avatar src='https://farm5.staticflickr.com/4531/38649907436_946ed319d4_o_d.jpg' />
                          <List.Content>
                             Get out of bed
                          </List.Content>
                        </List.Item>

                        <List.Item>
                          <List.Content floated='right'>
                            <Icon name='zoom' />
                          </List.Content>
                          <Image avatar src='https://farm5.staticflickr.com/4531/38649907436_946ed319d4_o_d.jpg' />
                          <List.Content>
                             Tie shoelace
                          </List.Content>
                        </List.Item>
                        <List.Item>
                          <List.Content floated='right'>
                            <Icon name='zoom' />
                          </List.Content>
                          <Image avatar src='https://farm5.staticflickr.com/4531/38649907436_946ed319d4_o_d.jpg' />
                          <List.Content>
                            Walk to school
                          </List.Content>
                        </List.Item>

                        <List.Item>
                          <List.Content floated='right'>
                            <Icon name='add circle' />
                          </List.Content>

                        </List.Item>
                        <List.Item>
                          <List.Content>
                            <Card centered>
                            <Card.Content>
                              <Card.Header>
                                Task Name:  <Input placeholder='Task Name' />
                              </Card.Header>
                              <Card.Description>
                                <Dropdown placeholder='choose time distribution' selection options={options} />
                                <Input placeholder='Least Time' />
                                <Input placeholder='Most Time' />
                                <Input placeholder='Most Likely Time' />
                              </Card.Description>
                            </Card.Content>

                            </Card>
                          </List.Content>

                        </List.Item>
                     </List>
                   </Grid.Column>
                   <Grid.Column width = {3}>

                   </Grid.Column>
                 </Grid.Row>
                 </Grid>
                 <div className="logOut">
                    <Link to="/" onClick={this.logOut}>
                      <Button>Back</Button>
                    </Link>
                </div>
                </div>
              </div>

            )

    }
}

export default Dashboard
