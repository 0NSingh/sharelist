"use client"
import { Button, ButtonType } from "@/components/button";
import { Heading } from "@/components/heading";
import { TextArea } from "@/components/input-components/text-area";
import { StatusBadge } from "@/components/status-badge";
import { FC } from "react";
interface  ListItemProps {

};

export const ListItem: FC< ListItemProps> = (props) => {
    return (
        <div className="w-full h-full border-2 rounded-2xl border-white">
        <Heading text={"Heading"}/>
        
        <StatusBadge label={"Created"}/>
       
        <li>
    list item 1
<TextArea/></li>            
     
     <div className={"flex gap-4 justify-center"}>
        <Button 
            onClick={()=>{}}
            type={ButtonType.Primary}
            label={"Save"}
            />
        <Button
            onClick={()=>{}}
            type={ButtonType.Primary}
            label={"Share"}
            />
     </div>
        </div>
    );
}
