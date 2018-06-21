var NameInput = React.createClass({displayName: "NameInput",
    handleTextChange: function(){
        var x = this.refs.nameField.getDOMNode().value;
        
        if(x != ''){
            this.refs.nameField.getDOMNode().className = 'active';
        } else {
            this.refs.nameField.getDOMNode().className = '';
        }

        this.props.onUserInput(x);
    },
    render: function(){
        return (
            React.createElement("div", {className: "control"}, 
                React.createElement("input", {type: "text", id: "comment", name:"comment", ref: "nameField", placeholder: "Watsonに話しかけましょう", autoFocus: true, required: true, onChange: this.handleTextChange}), 
                React.createElement("label", {for: "name"}, "コメント入力")
            )
        )
    }
});

var Checkbox = React.createClass({
  getInitialState: function() {
    return {checked: true}
  },
  handleCheck: function() {
    this.setState({checked: !this.state.checked});
    this.setState({value: "OFF"})
  },
  render: function() {
    var msg;
    if (this.state.checked) {
      msg = "checked";
    } else {
      msg = "unchecked";
    }
    return (
/*      <div>
        <input type="checkbox" onChange={this.handleCheck} defaultChecked={this.state.checked}/>
        <p>this box is {msg}.</p>
      </div>*/""
    );
  }
});

var LanguageInput = React.createClass({displayName: "LanguageInput",


  getInitialState: function() {
    return {checked: true}
  },
  handleCheck: function() {
  },
    render: function(){
        return (
            React.createElement("input", {type: "checkbox", className: "toggle_button", dataofflabel: "OFF", dataonlabel: "ON", id:"language", name:"language", value: "ON", onChange: this.handleCheck}
//    <input type="checkbox" class="toggle_button2" dataofflabel="OFF" dataonlabel="ON">
            )
        )
    }
});


var ContactForm = React.createClass({displayName: "夏のオープンキャンパス",
    getInitialState: function() {
        return {
            nameText: '',
            emailText: '',
            messageText: ''
            
        };
    },
    handleUserInput: function(nameText, emailText, messageText) {
        this.setState({
            nameText: nameText,
            emailText: emailText,
            messageText: messageText
        });
    },
  render: function(){
    return (
         React.createElement("form", {method: "POST"}, 
        
            React.createElement("fieldset", null, 
                React.createElement("legend", null, "高度ITエンジニア科　体験実習"), 
                
                React.createElement(LanguageInput, {onChange: this.handleCheck}), 
                //React.createElement(Checkbox, {}), 
                React.createElement(NameInput, {onUserInput: this.handleUserInput}), 
                React.createElement("input", {type: "submit", value: "送信"})
            )

        )
        );
  }
});

React.render(React.createElement(ContactForm, null), document.getElementById('stage'));