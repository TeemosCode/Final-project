import React, { Component } from 'react'
import { Button, Card, Menu, activeItem, Container, Image, Header, Segment, Grid, List, Divider, Icon, Input, Dropdown, Modal, Form, Select } from 'semantic-ui-react'
import { Link } from 'react-router-dom'
import axios from 'axios'

import styles from './styles.scss'
const options = [
  { key: 'Normal', text: 'Normal', value: 'Normal' },
  { key: 'PERT', text: 'PERT', value: 'PERT' },
  { key: 'Uniform', text: 'Uniform', value: 'Uniform' }
]
var taskItems = [
  {
    "task_name" : "Get out of bed",
    "value" : "Normal",
    "mean" : "4",
    "standard_deviation" : "0.9",
    "worst_case" : null,
    "most_likely_case" : null,
    "best_case" : null,
    "max_value" : null,
    "min_value" : null
  },
  {
    "task_name" : "Tie shoelace",
    "value" : "PERT",
    "mean" : null,
    "standard_deviation" : null,
    "worst_case" : 5,
    "most_likely_case" : 1,
    "best_case" : 0.5,
    "max_value" : null,
    "min_value" : null
  },
  {
    "task_name" : "Walk to school",
    "value" : "Uniform",
    "mean" : null,
    "standard_deviation" : null,
    "worst_case" : null,
    "most_likely_case" : null,
    "best_case" : null,
    "max_value" : 30,
    "min_value" : 10
  }
];


class Dashboard extends Component {

    constructor(props) {
          super(props);
          this.state = {
            value: 'Choose',
            task_name: '',
            mean: '',
            standard_deviation: '',
            worst_case: '',
            most_likely_case: '',
            best_case: '',
            max_value: '',
            min_value: ''

          };

          this.allTasks = [];
          this.getTaskList = this.getTaskList.bind(this);
          this.getDistributionForm = this.getDistributionForm.bind(this);
          this.handleInputChange = this.handleInputChange.bind(this);
          this.handleSubmit = this.handleSubmit.bind(this);
    }

    getTaskList(){
      this.allTasks = taskItems.map((task)=>{

        return(
          <List.Item>
          <List.Content floated='right'>
            <Icon name='zoom' />
          </List.Content>
          <List.Content>
          {task.task_name}
          </List.Content>
        </List.Item>
        )
      })
    }

    getDistributionForm(){
          if (this.state.value == "Normal"){
            return(
              <Form.Group widths='equal'>
                <Form.Field>
                  <label>Mean</label>
                  <Input
                    placeholder='Mean'
                    name='mean'
                    value={this.state.mean}
                    onChange={this.handleInputChange}
                     />
                </Form.Field>
                <Form.Field>
                  <label>Standard_deviation</label>
                  <Input
                    placeholder='Standard_deviation'
                    name='standard_deviation'
                    value={this.state.standard_deviation}
                    onChange={this.handleInputChange}
                     />
                </Form.Field>
              </Form.Group>
            )
          }else if (this.state.value == "PERT") {
            return(
              <Form.Group widths='equal'>
                <Form.Field>
                  <label>Worst Case</label>
                  <Input
                    placeholder='Worst Case'
                    name='worst_case'
                    value={this.state.worst_case}
                    onChange={this.handleInputChange}
                     />
                </Form.Field>
                <Form.Field>
                  <label>Most Likely Case</label>
                  <Input
                    placeholder='Most Likely Case'
                    name='most_likely_case'
                    value={this.state.most_likely_case}
                    onChange={this.handleInputChange}
                     />
                </Form.Field>
                <Form.Field>
                  <label>Best Case</label>
                  <Input
                    placeholder='Best Case'
                    name='best_case'
                    value={this.state.best_case}
                    onChange={this.handleInputChange}
                     />
                </Form.Field>
              </Form.Group>
            )
          }else if (this.state.value == "Uniform") {
            return(
              <Form.Group widths='equal'>
                <Form.Field>
                  <label>Max Value</label>
                  <Input
                    placeholder='Max Value'
                    name='max_value'
                    value={this.state.max_value}
                    onChange={this.handleInputChange}
                     />
                </Form.Field>
                <Form.Field>
                  <label>Min Value</label>
                  <Input
                    placeholder='Min Value'
                    name='min_value'
                    value={this.state.min_value}
                    onChange={this.handleInputChange}
                     />
                </Form.Field>
              </Form.Group>
            )
          }else {
            return null;
          }
    }
    handleInputChange(event) {
      const value = event.target.value;
      const name = event.target.name;

      this.setState({
        [name]: value
      });
      var inputs = {[name]: value};
      console.log(event.target);

    }


    handleSubmit(event) {
      // alert('A name was submitted: ' + this.state.task_name);
      // alert('A mean was submitted: ' + this.state.mean);
      var new_task = {};
      new_task.task_name = this.state.task_name;
      new_task.value = this.state.value;
      new_task.mean = this.state.mean;
      new_task.standard_deviation = this.state.standard_deviation;
      new_task.worst_case = this.state.worst_case;
      new_task.most_likely_case = this.state.most_likely_case;
      new_task.best_case = this.state.best_case;
      new_task.max_value = this.state.max_value;
      new_task.min_value = this.state.min_value;
      taskItems.push(new_task);
      console.log(taskItems);
      this.setState({});
    }
    render() {
            this.getTaskList();
            this.distributionForm = this.getDistributionForm();
            return(
              <div className = "Dashboard">


                <div>
                <Grid columns={3} divided>
                 <Grid.Row>
                   <Grid.Column width = {3}>
                   </Grid.Column>
                   <Grid.Column width = {8}>
                     <List divided verticalAlign='middle'>
                        {this.allTasks}

                        <Modal trigger={<Button>Add New Task</Button>} closeIcon>
                        <div className = "form">
                          <Form onSubmit={this.handleSubmit}>
                            <Form.Group widths='equal'>
                              <Form.Field>
                                <label>Task Name</label>
                                <Input
                                  placeholder='Task Name'
                                  name='task_name'
                                  value={this.state.task_name}
                                  onChange={this.handleInputChange}
                                   />
                              </Form.Field>
                              <Form.Field>
                                <label>Choose Time Distribution</label>
                                <Dropdown
                                  onChange={(e, { value }) => this.setState({ value })}
                                  name='value'
                                  value={this.state.value}
                                  placeholder='Choose Time Distribution'
                                  selection
                                  options={options}
                                 />
                              </Form.Field>
                            </Form.Group>
                            {this.distributionForm}

                            <Form.Field control={Button}>Submit</Form.Field>
                          </Form>
                        </div>
                        </Modal>
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
