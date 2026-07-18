import { Link, useLocation } from "react-router-dom";
import {
    FaHome,
    FaBook,
    FaCog,
    FaRobot
} from "react-icons/fa";

function Sidebar() {

    const location = useLocation();

    const menu = [

        {
            name: "Home",
            path: "/",
            icon: <FaHome />
        },

        {
            name: "Libraries",
            path: "/libraries",
            icon: <FaBook />
        },

        {
            name: "Settings",
            path: "/settings",
            icon: <FaCog />
        }

    ];

    return (

        <aside className="w-64 bg-slate-900 text-white flex flex-col">

            <div className="p-6 border-b border-slate-700">

                <div className="flex items-center gap-3">

                    <FaRobot size={28} />

                    <div>

                        <h2 className="font-bold text-lg">

                            Cigma

                        </h2>

                        <p className="text-xs text-slate-400">

                            Agentic Research Assistant

                        </p>

                    </div>

                </div>

            </div>

            <nav className="flex-1 mt-6">

                {menu.map((item) => (

                    <Link

                        key={item.path}

                        to={item.path}

                        className={`flex items-center gap-3 px-6 py-4 transition

                        ${
                            location.pathname === item.path

                            ? "bg-blue-600"

                            : "hover:bg-slate-800"

                        }`}

                    >

                        {item.icon}

                        {item.name}

                    </Link>

                ))}

            </nav>

        </aside>

    );

}

export default Sidebar;