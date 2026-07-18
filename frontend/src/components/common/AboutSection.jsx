import {
    FaGithub,
    FaLinkedin,
    FaGlobe,
    FaEnvelope,
    FaBrain,
    FaDatabase,
    FaRobot,
} from "react-icons/fa";

function AboutSection() {
    return (
        <section className="mt-20 bg-white rounded-3xl shadow-xl p-10">

            <div className="grid lg:grid-cols-2 gap-10 items-center">

                {/* Left */}

                <div>

                    <span className="text-blue-600 font-semibold uppercase tracking-widest">
                        About This Project
                    </span>

                    <h2 className="text-4xl font-bold text-slate-800 mt-3">
                        Cigma Agentic Research Assistant
                    </h2>

                    <p className="mt-6 text-gray-600 leading-8">
                        Cigma Agentic Research Assistant is an AI-powered
                        scientific research platform designed to accelerate
                        literature review, evidence synthesis, and research
                        report generation.
                    </p>

                    <p className="mt-4 text-gray-600 leading-8">
                        It combines Retrieval-Augmented Generation (RAG),
                        semantic search, local research libraries, and
                        real-time scientific literature retrieval to produce
                        professional evidence-based reports.
                    </p>

                </div>

                {/* Right */}

                <div>

                    <div className="bg-slate-50 rounded-2xl p-8">

                        <h3 className="text-2xl font-bold text-slate-800 mb-4">
                            Developed By
                        </h3>

                        <p className="text-xl font-semibold">
                            Badawi Amin Muhammed
                        </p>

                        <p className="text-gray-500 mb-6">
                            AI/ML Engineer • Data Scientist • Research Analyst
                        </p>

                        <div className="flex flex-wrap gap-3 mb-8">

                            <span className="bg-blue-100 text-blue-700 px-4 py-2 rounded-full flex items-center gap-2">
                                <FaRobot />
                                Agentic AI
                            </span>

                            <span className="bg-green-100 text-green-700 px-4 py-2 rounded-full flex items-center gap-2">
                                <FaBrain />
                                RAG
                            </span>

                            <span className="bg-purple-100 text-purple-700 px-4 py-2 rounded-full flex items-center gap-2">
                                <FaDatabase />
                                FAISS
                            </span>

                        </div>

                        <div className="space-y-4">

                            <a
                                href="https://github.com/e-badawy"
                                target="_blank"
                                rel="noreferrer"
                                className="flex items-center gap-3 text-gray-700 hover:text-blue-600"
                            >
                                <FaGithub />
                                GitHub
                            </a>

                            <a
                                href="https://linkedin.com/in/elameenbadawy"
                                target="_blank"
                                rel="noreferrer"
                                className="flex items-center gap-3 text-gray-700 hover:text-blue-600"
                            >
                                <FaLinkedin />
                                LinkedIn
                            </a>

                            <a
                                href="https://e-badawy.github.io"
                                target="_blank"
                                rel="noreferrer"
                                className="flex items-center gap-3 text-gray-700 hover:text-blue-600"
                            >
                                <FaGlobe />
                                Portfolio
                            </a>

                            <a
                                href="mailto:officialbadawy@email.com"
                                className="flex items-center gap-3 text-gray-700 hover:text-blue-600"
                            >
                                <FaEnvelope />
                                Email
                            </a>

                        </div>

                    </div>

                </div>

            </div>

        </section>
    );
}

export default AboutSection;