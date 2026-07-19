import { useState } from "react";
import api from "../api/api";
import ReportViewer from "../components/chat/ReportViewer";
import useLibrary from "../hooks/useLibrary";
import { motion } from "framer-motion";
import AboutSection from "../components/common/AboutSection";
import Footer from "../components/common/Footer";
import LoadingPipeline from "../components/common/LoadingPipeline";
import ExportToolbar from "../components/export/ExportToolbar";
import { useResearch } from "../context/ResearchContext";

import {
    FaRobot,
    FaArrowRight,
    FaBookOpen
} from "react-icons/fa";

function Home() {
    const [question, setQuestion] = useState("");
    const [library, setLibrary] = useState("");
    const [searchWeb, setSearchWeb] = useState(true);

    const [loading, setLoading] = useState(false);

    const { report, setReport } = useResearch();

    const {libraries} = useLibrary();

    const generateResearch = async () => {
        if (!question.trim()) {
            alert("Please enter a research question.");
            return;
        }

        try {
            setLoading(true);

            const response = await api.post("/agent", {
                question,
                library_name: library,
                search_web: searchWeb,
            });
            console.log("Agent Response:", response.data);
            setReport(response.data);
            
        } catch (error) {
            console.error(error);
            alert("Failed to generate report.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="bg-slate-50 min-h-screen">

            {/* Workspace */}

            <motion.div

            
                initial={{ opacity: 0, y: 30 }}

                animate={{ opacity: 1, y: 0 }}

                transition={{ duration: 0.5 }}

                className="rounded-3xl bg-gradient-to-r from-blue-700 via-indigo-700 to-slate-900 text-white shadow-2xl p-10"

            >

                <div className="flex flex-col lg:flex-row justify-between items-center gap-8">

                    <div className="max-w-3xl">

                        <div className="flex items-center gap-4 mb-6">

                            <div className="bg-white/20 p-4 rounded-2xl">

                                <FaRobot size={32} />

                            </div>

                            <div>

                                <h1 className="text-4xl font-extrabold">

                                     Cigma Agentic Research Assistant

                                </h1>

                                <p className="text-blue-100 mt-2">

                                    Accelerating Scientific Discovery with Agentic AI

                                </p>

                            </div>

                        </div>

                        <p className="text-lg leading-8 text-blue-50">

                            Generate professional evidence-based research reports by combining

                            your private research library, semantic retrieval, and the latest

                            scientific literature from trusted sources.

                        </p>

                        <div className="flex flex-wrap gap-4 mt-8">

                            <button

                                className="bg-white text-blue-700 px-6 py-3 rounded-xl font-semibold flex items-center gap-2 hover:scale-105 transition"

                            >

                                <FaArrowRight />

                                Ask Anything

                            </button>

                            <button

                                className="border border-white px-6 py-3 rounded-xl flex items-center gap-2 hover:bg-white hover:text-blue-700 transition"

                            >

                                <FaBookOpen />

                                    Build Research Library

                            </button>

                        </div>

                    </div>

                    <div>

                        <img

                            src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=700"

                            alt="AI"

                            className="rounded-2xl shadow-xl w-[420px]"

                        />

                    </div>

                </div>

            </motion.div>

            <div className="h-8"></div>

            <div className="bg-white rounded-2xl shadow-lg p-8">

                <div className="space-y-6">

                    <div>

                        <label className="block font-semibold mb-2">
                            Research Question
                        </label>

                        <textarea
                            rows={8}
                            className="w-full rounded-xl border border-gray-300 p-4 focus:outline-none focus:ring-2 focus:ring-blue-500"
                            placeholder="Example: How does tuberculosis alter the gut microbiome in pregnant women, and what are the latest findings?"
                            value={question}
                            onChange={(e) => setQuestion(e.target.value)}
                        />

                    </div>

                    <div className="grid md:grid-cols-2 gap-6">

                        <div>

                            <label className="block font-semibold mb-2">
                                Research Library
                            </label>

                            <select
                                value={library}
                                onChange={(e) => setLibrary(e.target.value)}
                                className="w-full rounded-xl border border-gray-300 p-3"
                            >

                                <option value="">
                                    Select Library
                                </option>

                                {

                                    libraries.map((lib) => (

                                        <option
                                            key={lib.library_name}
                                            value={lib.library_name}
                                        >

                                            {lib.library_name}

                                        </option>

                                    ))

                                }

                            </select>

                        </div>

                        <div className="flex items-end">

                            <label className="flex items-center gap-3">

                                <input
                                    type="checkbox"
                                    checked={searchWeb}
                                    onChange={(e) =>
                                        setSearchWeb(e.target.checked)
                                    }
                                />

                                Search Latest Scientific Literature

                            </label>

                        </div>

                    </div>

                    <button
                        onClick={generateResearch}
                        disabled={loading}
                        className="bg-blue-600 hover:bg-blue-700 disabled:bg-gray-400 text-white px-8 py-4 rounded-xl font-semibold transition"
                    >
                        {loading
                            ? "Generating Report..."
                            : "Generate Research Report"}
                    </button>

                </div>

        </div>

            {/* AI REPORT */}

            <div className="bg-white rounded-3xl border border-slate-200 shadow-xl mt-10 p-10">

                <h2 className="text-2xl font-bold mb-6 text-slate-800">
                     AI Research Report
                </h2>

                {loading && <LoadingPipeline />}

                <ExportToolbar report={report} />

                <ReportViewer answer={report?.answer} />

            </div>

        <AboutSection />


</div>
);
}

export default Home;