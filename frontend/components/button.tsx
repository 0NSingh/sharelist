import { FC } from "react";
export enum ButtonType {
  Primary = 'primary',
  Secondary = 'secondary',
  Danger = 'danger',
}
interface  ButtonProps {
    label:string;
    onClick:()=>void;
    type:ButtonType
};

export const Button: FC< ButtonProps> = (props) => {
    return (
        <div className="">
            <button onClick={props.onClick}>
                {props.label}
            </button>
        </div>
    );
}
