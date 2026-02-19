import { SideBar } from "@/components/sidebar";
import { ListItem } from "./_components/list-item";
import { AppBar } from "@/components/app-bar";
import { PaginationBar } from "@/components/pagination-bar";
import { OptionsBar } from "@/components/options-bar";
import { ListWindow } from "./_components/list-window";

export default function MyList(){
    return (
    <div>
    <div className="w-full h-full flex gap-2">
    <SideBar/>
    <div className="w-full h-full gap-2">

        <AppBar/>
        <ListWindow/>
    </div>
    <div className="w-1/3 h-full border-2 border-white p-4"></div>
    </div>
    </div>
    )
}