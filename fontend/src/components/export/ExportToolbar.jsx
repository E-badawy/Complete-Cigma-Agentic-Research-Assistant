import {

FaFilePdf,

FaFileWord,

FaCopy,

FaMarkdown

} from "react-icons/fa";

import {

copyReport,

downloadMarkdown,

downloadPDF,

downloadWord

} from "../../services/exportApi";

function ExportToolbar({ report }) {

    if (!report) return null;

    const text = report.answer;

    return (

        <div className="flex flex-wrap gap-4 mb-8">

            <button

                onClick={() => downloadPDF(text)}

                className="px-5 py-3 rounded-xl border hover:bg-red-50"

            >

                <FaFilePdf />

                PDF

            </button>

            <button

                onClick={() => downloadWord(text)}

                className="px-5 py-3 rounded-xl border hover:bg-blue-50"

            >

                <FaFileWord />

                Word

            </button>

            <button

                onClick={() => copyReport(text)}

                className="px-5 py-3 rounded-xl border"

            >

                <FaCopy />

                Copy

            </button>

            <button

                onClick={() => downloadMarkdown(text)}

                className="px-5 py-3 rounded-xl border"

            >

                <FaMarkdown />

                Markdown

            </button>

        </div>

    );

}

export default ExportToolbar;