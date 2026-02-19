import { FC } from "react";
interface  StatusBadgeProps {
    label:string;
};

export const StatusBadge: FC< StatusBadgeProps> = (props) => {
    return (
        <div>
            <span className={"w-28 h-full bg-white/50 border-1 border-white justify-self-end items-self-end align rounded-full p-2 m-1 flex"}><div ></div>{props.label}<div></div></span>
        </div>
    );
}
