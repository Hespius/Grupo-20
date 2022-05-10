import { Component } from "react";
import "./button.css";

class Button extends Component {
    renderType = (classStyle) => {
        if(classStyle === "secondary") {
            return "btn secondary";
        } else if (classStyle === "dark") {
            return "btn dark";
        } else {
            return "btn btn-primary";
        }
      };

    render() {
        const { text, onClick, type, style, classType, disabled } = this.props;
        return (
          <button
            className={this.renderType(classType)}
            type={type === "submit" ? "submit" : "button"}
            onClick={onClick}
            disabled={disabled}
            style={style}
          >
            <p className="pure-menu-link flex-center">
                {text}
            </p>
          </button>
        );
      }
}

export default Button;