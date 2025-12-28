export default function MyList(){
    return (
    <div className="w-full h-full p-4">
        <h1>
            Heading
        </h1>
            <ul>
        <li>
    list item 1
    sub list item
    description( text)
    status
       </li>       
    <li>
    list item 2
    sub list item
    description(2 text)
    status
    </li>       
        
     </ul>
     <div>
        <button>
            save
        </button>
        <br/>
        <button>
            share(download(pdf), share via link, share via text)
        </button>
     </div>
    </div>
    )
}