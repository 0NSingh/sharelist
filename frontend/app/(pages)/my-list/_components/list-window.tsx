import { OptionsBar } from "@/components/options-bar";
import { FC } from "react";
import { ListItem } from "./list-item";
import { PaginationBar } from "@/components/pagination-bar";
interface  ListWindowProps {};

export const ListWindow: FC< ListWindowProps> = (props) => {
    return (
        
        <div className="w-full h-1/2">
          <ListItem/>
        
    <ListItem/>

    
    </div>
    );
}
