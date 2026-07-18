import {
    FaGithub,
    FaLinkedin,
    FaGlobe,
    FaEnvelope,
} from "react-icons/fa";

function Footer() {
    return (
        <footer className="bg-slate-950 text-gray-300 mt-24">

            <div className="max-w-7xl mx-auto px-8 py-16">

                <div className="flex flex-col lg:flex-row justify-between gap-10">

                    <div className="max-w-lg">

                        <h2 className="text-2xl font-bold text-white">
                            Cigma Agentic Research Assistant
                        </h2>

                        <p className="mt-5 leading-8 text-gray-400">
                            Intelligent scientific research powered by
                            Retrieval-Augmented Generation, semantic search,
                            and state-of-the-art language models.
                        </p>

                    </div>

                    <div>

                        <h3 className="font-semibold text-white mb-4">
                            Quick Links
                        </h3>

                        <div className="space-y-3">

                            <a href="#" className="hover:text-white">
                                Home
                            </a>

                            <br />

                            <a href="#" className="hover:text-white">
                                Libraries
                            </a>

                            <br />

                            <a href="#" className="hover:text-white">
                                Settings
                            </a>

                        </div>

                    </div>

                    <div>

                        <h3 className="font-semibold text-white mb-4">
                            Connect
                        </h3>

                        <div className="flex gap-5 text-2xl">

                            <a href="#">
                                <FaGithub />
                            </a>

                            <a href="#">
                                <FaLinkedin />
                            </a>

                            <a href="#">
                                <FaGlobe />
                            </a>

                            <a href="#">
                                <FaEnvelope />
                            </a>

                        </div>

                    </div>

                </div>

                <div className="border-t border-slate-800 mt-12 pt-8 flex flex-col md:flex-row justify-between">

                    <span>
                        © 2026 Cigma General Solutions
                    </span>

                    <span>
                        Designed & Developed by
                        <span className="font-semibold text-white">
                            {" "}Badawi Aminu Muhammed
                        </span>
                    </span>

                </div>

            </div>

        </footer>
    );
}

export default Footer;