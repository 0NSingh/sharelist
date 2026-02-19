import { FC } from "react";
interface  TextAreaProps {

};

export const TextArea: FC< TextAreaProps> = (props) => {
    return (
        <div>    <textarea defaultValue={"Description of the task"} aria-label="description-text" className="bg-white">
        
            </textarea>     
        </div>
    );
}
