import { Outlet } from "react-router-dom";
import Sidebar from "../components/sidebar/Sidebar";
import Topbar from "../components/common/Topbar";
import SourcesPanel from "../components/sources/SourcesPanel";
import { useResearch } from "../context/ResearchContext";

function MainLayout() {

    const { report } = useResearch();

    return (

        <div className="h-screen flex bg-slate-100">

            <Sidebar />

            <div className="flex flex-col flex-1">

                <Topbar />

                <main className="flex flex-1 overflow-hidden">

                    <section className="flex-1 overflow-y-auto p-6">

                        <Outlet />

                    </section>

                    <aside className="hidden xl:block w-[380px] border-l bg-white overflow-y-auto">

                        <SourcesPanel

                            localSources={report?.local_sources || []}

                            webSources={report?.web_sources || []}

                            references={report?.references || []}

                        />

                    </aside>

                </main>

            </div>

        </div>

    );

}

export default MainLayout;