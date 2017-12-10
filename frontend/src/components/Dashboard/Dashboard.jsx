import React, { Component } from 'react'
import { Button, Card, Menu, activeItem, Table, Container, Rating, Image, Header, Segment, Grid, List, Divider, Icon, Input, Dropdown, Modal, Form, Select } from 'semantic-ui-react'
import { Link } from 'react-router-dom'
import axios from 'axios'

import styles from './styles.scss'
const options = [
  { key: 'Normal', text: 'Normal', value: 'Normal' },
  { key: 'PERT', text: 'PERT', value: 'PERT' },
  { key: 'Uniform', text: 'Uniform', value: 'Uniform' }
]
var taskItems = [

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
            min_value: '',
            outerModalOpen: false,
            innerModalOpen: false

          };

          this.taskTable = [];
          this.getTable = this.getTable.bind(this);
          this.getDistributionForm = this.getDistributionForm.bind(this);
          this.handleInputChange = this.handleInputChange.bind(this);
          this.handleSubmit = this.handleSubmit.bind(this);
    }

    //put all the task items into task table, then the table will render in the page
    getTable(){
      this.taskTable = taskItems.map((task)=>{

        return(
          <Table.Row>
            <Table.Cell>{task.task_name}</Table.Cell>
            <Table.Cell>{task.value}</Table.Cell>
            <Table.Cell>{task.mean}</Table.Cell>
            <Table.Cell>{task.standard_deviation}</Table.Cell>
            <Table.Cell>{task.worst_case}</Table.Cell>
            <Table.Cell>{task.most_likely_case}</Table.Cell>
            <Table.Cell>{task.best_case}</Table.Cell>
            <Table.Cell>{task.max_value}</Table.Cell>
            <Table.Cell>{task.min_value}</Table.Cell>

          </Table.Row>
        )
      })
    }
    getDistributionForm(){
      //if you press normal distribution, the value is "Normal", then it will only appear mean and sd

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
            //if you press PERT distribution, the value is "PERT", then it will only appear worst_case, most_likely_case and best_case

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
            //if you press Uniform distribution, the value is "Uniform", then it will only appear max_value and min_value

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
    //if you input something in the blank, the input will immediately show in the blank
    handleInputChange(event) {
      const value = event.target.value;
      const name = event.target.name;

      this.setState({
        [name]: value
      });
      var inputs = {[name]: value};
      // console.log(event.target);

    }

    //after you submit something, it will produce a new task, and set the new task's name or value ... into the value of the new tasks
    //Then push the new task into the taskItems, which will show in the task table
    //After you push the new_task, rerender the page, and set the innerModalOpen true to show the innerModal, which says "You have submitted one task, do you want to add more?"
    // then make the state of task_name, mean, ... to be '', so that user can input other task names and means...
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
      this.setState({ innerModalOpen: true })
      this.setState({
        value: 'Choose',
        task_name: '',
        mean: '',
        standard_deviation: '',
        worst_case: '',
        most_likely_case: '',
        best_case: '',
        max_value: '',
        min_value: ''
      });
    }
    //render the homepage
    //after you press the button "Add New Task", a modal, which is a form for users to enter task name, mean, distribution,... , will be shown.
    //after you click the button "Submit", it trigers the innerModal
    render() {
            this.getTable();
            this.distributionForm = this.getDistributionForm();
            //set the modal's style
            const modal = {
              textAlign: 'center'
            };
            return(
              <div className = "Dashboard">
                <div className = "page">
                        <div className = "table">
                        <Table color='blue' textAlign='center'>
                          <Table.Header>
                            <Table.Row>
                              <Table.HeaderCell>Task Name</Table.HeaderCell>
                              <Table.HeaderCell>Distribution</Table.HeaderCell>
                              <Table.HeaderCell>Mean</Table.HeaderCell>
                              <Table.HeaderCell>Standard_deviation</Table.HeaderCell>
                              <Table.HeaderCell>Worst Case</Table.HeaderCell>
                              <Table.HeaderCell>Most Likely Case</Table.HeaderCell>
                              <Table.HeaderCell>Best Case</Table.HeaderCell>
                              <Table.HeaderCell>Max Value</Table.HeaderCell>
                              <Table.HeaderCell>Min Value</Table.HeaderCell>
                            </Table.Row>
                          </Table.Header>

                          <Table.Body>
                          {this.taskTable}
                          </Table.Body>
                        </Table>
                        </div>
                        <div className = "modal">
                        <Modal
                          trigger={<Button basic style = {modal} color='blue' onClick={() => this.setState({ outerModalOpen: true })}>Add New Task</Button>}
                          open={this.state.outerModalOpen}
                          onClose={() => this.setState({ outerModalOpen: false })}
                          closeIcon
                        >

                        <div className = "form">
                          <Form>
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

                          </Form>
                        </div>
                        <Modal.Actions>
                          <Modal
                            trigger={<Button onClick={this.handleSubmit}>Submit</Button>}
                            open={this.state.innerModalOpen}
                            onClose={() => this.setState({ innerModalOpen: false })}
                          >
                            <Header icon='archive' content='Successfully submitted' />

                            <Modal.Content>
                              <p>You have submitted one task, do you want to add more?</p>
                            </Modal.Content>
                            <Modal.Actions>
                              <Button basic color='red' onClick={() => this.setState({ innerModalOpen: false, outerModalOpen: false })}>
                                <Icon name='remove' /> No
                              </Button>
                              <Button color='green' onClick={() => this.setState({ innerModalOpen: false })}>
                                <Icon name='checkmark' /> Yes
                              </Button>
                            </Modal.Actions>
                          </Modal>
                        </Modal.Actions>
                        </Modal>
                        </div>
                        <Button.Group floated='right'>
                          <Button>
                            <Icon name='play' />Run simulation
                          </Button>
                              <Link to="/" onClick={this.logOut}>
                                <Button>Back</Button>
                              </Link>
                            </Button.Group>
                </div>
              </div>

            )

    }
}

export default Dashboard
