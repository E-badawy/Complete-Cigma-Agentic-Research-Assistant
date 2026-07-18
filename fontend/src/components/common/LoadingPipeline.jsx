import { motion } from "framer-motion";

import {
    FaSearch,
    FaDatabase,
    FaGlobe,
    FaBrain,
    FaPenFancy,
    FaBook
} from "react-icons/fa";

const steps = [
    {
        icon: <FaSearch />,
        text: "Understanding your research question..."
    },
    {
        icon: <FaDatabase />,
        text: "Searching your knowledge library..."
    },
    {
        icon: <FaGlobe />,
        text: "Retrieving latest scientific literature..."
    },
    {
        icon: <FaBrain />,
        text: "Ranking and synthesizing evidence..."
    },
    {
        icon: <FaPenFancy />,
        text: "Writing professional report..."
    },
    {
        icon: <FaBook />,
        text: "Formatting citations and references..."
    }
];

function LoadingPipeline() {

    return (

        <div className="bg-white rounded-3xl shadow-xl p-8 mt-8">

            <h2 className="text-2xl font-bold text-slate-800">

                🤖 Cigma is conducting research...

            </h2>

            <p className="text-gray-500 mt-2 mb-8">

                Please wait while AI searches and analyses scientific evidence.

            </p>

            <div className="space-y-6">

                {steps.map((step,index)=>(

                    <motion.div

                        key={index}

                        initial={{opacity:0,x:-20}}

                        animate={{opacity:1,x:0}}

                        transition={{delay:index*0.45}}

                        className="flex items-center gap-5"

                    >

                        <div className="w-12 h-12 rounded-full bg-blue-600 text-white flex items-center justify-center animate-pulse">

                            {step.icon}

                        </div>

                        <div className="flex-1">

                            <div className="font-medium">

                                {step.text}

                            </div>

                            <div className="h-1 rounded bg-blue-100 mt-2 overflow-hidden">

                                <motion.div

                                    className="h-full bg-blue-600"

                                    animate={{width:["0%","100%"]}}

                                    transition={{
                                        repeat:Infinity,
                                        duration:2
                                    }}

                                />

                            </div>

                        </div>

                    </motion.div>

                ))}

            </div>

        </div>

    );

}

export default LoadingPipeline;