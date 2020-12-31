import dev.technici4n.fasttransferlib.api.context.Context;
import dev.technici4n.fasttransferlib.impl.context.TransactionContext;

import java.util.*;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public final class GlobalTransferTransaction {
    private static final boolean CHECK = true;
    private static final Deque<GlobalTransactionImpl> DEQUE = new ArrayDeque<>(16);
    private static Thread serverThread = null;
    private static final Lock OUTER_LOCK = new ReentrantLock();
    private static final Lock INNER_LOCK = new ReentrantLock();

    private GlobalTransferTransaction() {
        throw new AssertionError();
    }

    public static void setServerThread(Thread serverThread) {
        if (GlobalTransferTransaction.serverThread != null) throw new AssertionError();
        GlobalTransferTransaction.serverThread = serverThread;
    }

    public static Context open() {
        assert serverThread != null;
        if (!Thread.currentThread().equals(serverThread))
            OUTER_LOCK.lock();
        INNER_LOCK.lock();

        GlobalTransactionImpl opened = new GlobalTransactionImpl(1L);
        DEQUE.push(opened);
        return opened;
    }

    public static void commit()
            throws NoSuchElementException {
        GlobalTransactionImpl current = DEQUE.pop(); // throws NoSuchElementException if there is nothing
        GlobalTransactionImpl parent = DEQUE.poll();
        DEQUE.push(current);
        if (parent == null) // not nested
            current.commit();
        else // nested
            current.commitWith(parent);
    }

    private static void close() {
        DEQUE.pop();
    }

    private static class GlobalTransactionImpl
            extends TransactionContext {
        public GlobalTransactionImpl(long estimatedActions) {
            super(estimatedActions);
        }

        @Override
        public void configure(Runnable action, Runnable reaction) {
            ensureActive(this);
            super.configure(action, reaction);
        }

        @Override
        public void execute(Runnable action) {
            ensureActive(this);
            super.execute(action);
        }

        @Override
        protected void commitReversibly() {
            ensureActive(this);
            if (CHECK && isCommitted()) throw new AssertionError(); // already committed
            super.commitReversibly();
        }

        @Override
        public void close() {
            ensureActive(this);
            GlobalTransferTransaction.close();
            super.close();

            INNER_LOCK.unlock();
            if (!Thread.currentThread().equals(serverThread))
                OUTER_LOCK.unlock();
        }

        protected static void ensureActive(GlobalTransactionImpl instance) {
            if (CHECK && !instance.equals(DEQUE.poll())) throw new AssertionError(); // inactive, no modification allowed
        }
    }

    private static class Example {
        static {
            setServerThread(Thread.currentThread());

            try (Context outermost = open()) {
                outermost.configure(() -> {}, () -> {});

                try (Context intermediate = open()) {
                    intermediate.configure(() -> {}, () -> {});

                    try (Context innermost = open()) {
                        innermost.configure(() -> {}, () -> {});
                        innermost.execute(() -> {});
                        commit();
                    }

                    intermediate.execute(() -> {});

                    if (new Random().nextBoolean())
                        commit();
                }
                commit();
            }
        }
    }
}
