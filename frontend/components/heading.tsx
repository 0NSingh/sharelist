import { FC } from "react";
interface  HeadingProps {
    text:string;

};

export const Heading: FC< HeadingProps> = (props) => {
    return (
        <div>
            <h1 className="text-3xl font-bold">
            {props.text}
        </h1>
        </div>
    );
}
