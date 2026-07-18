import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

function ReportViewer({ answer }) {

    if (!answer) {

        return (

            <div className="text-gray-400 italic text-center py-20">

                Your AI-generated research report will appear here.

            </div>

        );

    }

    return (

        <article
            className="
                prose
                prose-lg
                max-w-none

                prose-headings:font-bold
                prose-headings:text-slate-900

                prose-h1:text-4xl
                prose-h1:border-b
                prose-h1:pb-3
                prose-h1:mb-8

                prose-h2:text-3xl
                prose-h2:mt-12
                prose-h2:text-blue-700

                prose-h3:text-2xl
                prose-h3:text-slate-800

                prose-p:text-gray-700
                prose-p:leading-8

                prose-strong:text-slate-900

                prose-ul:my-5
                prose-ol:my-5

                prose-li:my-2

                prose-blockquote:border-l-4
                prose-blockquote:border-blue-600
                prose-blockquote:bg-blue-50
                prose-blockquote:px-4
                prose-blockquote:py-2

                prose-table:border
                prose-th:bg-slate-100

                prose-code:text-pink-600
                prose-pre:bg-slate-900
            "
        >

            <ReactMarkdown remarkPlugins={[remarkGfm]}>

                {answer}

            </ReactMarkdown>

        </article>

    );

}

export default ReportViewer;